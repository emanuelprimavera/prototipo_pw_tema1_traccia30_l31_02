from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection

app = FastAPI(
    title="API Monitoraggio Industria 4.0/5.0 - Serigrafia",
    description="Back-end FastAPI per il calcolo dei KPI economico-operativi",
    version="1.0.0"
)

# Configurazione CORS per permettere al fe di comunicare con il be
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Server FastAPI attivo e operativo per il Project Work L-31."}

@app.get("/api/macchinari")
def get_macchinari():
    """Restituisce l'anagrafica di tutte le stazioni di lavoro."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM macchinari")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/api/parametri")
def get_parametri():
    """Restituisce i parametri economici globali (costo energia, materia prima)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM costi_parametri")
    rows = cursor.fetchall()
    conn.close()
    return {row["chiave"]: row["valore"] for row in rows}

@app.get("/api/rilevazioni")
def get_rilevazioni():
    """Restituisce l'elenco completo delle rilevazioni di turno con dettagli macchina e turno."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            r.id,
            m.nome_macchina,
            m.tipo,
            m.costo_orario_fermo,
            t.data,
            t.nome_turno,
            r.pezzi_prodotti,
            r.pezzi_scarto,
            r.consumo_kwh,
            r.minuti_fermo,
            r.tempo_operativo_minuti
        FROM rilevazioni_turno r
        JOIN macchinari m ON r.macchinario_id = m.id
        JOIN turni_produzione t ON r.turno_id = t.id
        ORDER BY t.data DESC, t.id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/api/kpi-globali")
def get_kpi_globali():
    """Calcola i KPI economico-gestionali aggregati per il controllo di gestione."""
    conn = get_connection()
    cursor = conn.cursor()

    # Recuperiamo parametri globali
    cursor.execute("SELECT chiave, valore FROM costi_parametri")
    parametri = {row["chiave"]: row["valore"] for row in cursor.fetchall()}
    costo_kwh = parametri.get("costo_kwh", 0.25)
    costo_materia = parametri.get("costo_materia_prima", 4.50)

    # Recuperiamo tutte le rilevazioni con i relativi costi macchina
    cursor.execute("""
        SELECT 
            r.pezzi_prodotti,
            r.pezzi_scarto,
            r.consumo_kwh,
            r.minuti_fermo,
            m.costo_orario_fermo
        FROM rilevazioni_turno r
        JOIN macchinari m ON r.macchinario_id = m.id
    """)
    rilevazioni = cursor.fetchall()
    conn.close()

    totale_pezzi = sum(r["pezzi_prodotti"] for r in rilevazioni)
    totale_scarti = sum(r["pezzi_scarto"] for r in rilevazioni)
    totale_kwh = sum(r["consumo_kwh"] for r in rilevazioni)
    
    # Calcoli finanziari ed economico-gestionali
    costo_totale_scarti = totale_scarti * costo_materia
    costo_totale_energia = totale_kwh * costo_kwh
    
    # Costo dei fermi macchina (minuti di fermo convertiti in ore * costo orario specifico)
    costo_totale_fermi = sum((r["minuti_fermo"] / 60.0) * r["costo_orario_fermo"] for r in rilevazioni)

    tasso_scarto_percentuale = (totale_scarti / totale_pezzi * 100) if totale_pezzi > 0 else 0.0

    return {
        "totale_pezzi_prodotti": totale_pezzi,
        "totale_pezzi_scarto": totale_scarti,
        "tasso_scarto_percentuale": round(tasso_scarto_percentuale, 2),
        "consumo_energetico_totale_kwh": round(totale_kwh, 2),
        "impatto_finanziario_scarti_eur": round(costo_totale_scarti, 2),
        "costo_totale_energia_eur": round(costo_totale_energia, 2),
        "costo_totale_fermi_macchina_eur": round(costo_totale_fermi, 2)
    }