import random
from database import get_connection, inizializza_database

def popola_dati_iniziali():
    # controllo esistenza table
    inizializza_database()
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Inserimento parametri economici globali (se non già presenti)
    parametri = [
        ('costo_kwh', 0.25, 'Costo dell\'energia elettrica in Euro al kWh'),
        ('costo_materia_prima', 4.50, 'Costo unitario del capo tessile grezzo in Euro')
    ]
    for chiave, valore, desc in parametri:
        cursor.execute(
            "INSERT OR IGNORE INTO costi_parametri (chiave, valore, descrizione) VALUES (?, ?, ?)",
            (chiave, valore, desc)
        )

    # 2. Inserimento anagrafica macchinari
    macchinari = [
        ('Stampante Serigrafica Automatica', 'Stampa', 65.0),
        ('Forno di Asciugatura UV', 'Asciugatura', 45.0),
        ('Stazione Controllo Qualità e Imballo', 'Imballo', 30.0)
    ]
    for nome, tipo, costo_fermo in macchinari:
        cursor.execute(
            "INSERT OR IGNORE INTO macchinari (id, nome_macchina, tipo, costo_orario_fermo) VALUES ((SELECT id FROM macchinari WHERE nome_macchina=?), ?, ?, ?)",
            (nome, nome, tipo, costo_fermo)
        )
        # Se la tabella era vuota, eseguiamo un semplice INSERT
        cursor.execute(
            "SELECT id FROM macchinari WHERE nome_macchina = ?", (nome,)
        )
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO macchinari (nome_macchina, tipo, costo_orario_fermo) VALUES (?, ?, ?)",
                (nome, tipo, costo_fermo)
            )

    # 3. Creazione di 5 turni di produzione simulati
    turni = [
        ('2026-03-01', 'Turno Mattina'),
        ('2026-03-01', 'Turno Pomeriggio'),
        ('2026-03-02', 'Turno Mattina'),
        ('2026-03-02', 'Turno Pomeriggio'),
        ('2026-03-03', 'Turno Mattina')
    ]
    
    # rimozione rilevazioni vecchie per evitare duplicazioni durante i test
    cursor.execute("DELETE FROM rilevazioni_turno")
    cursor.execute("DELETE FROM turni_produzione")

    for data_t, nome_t in turni:
        cursor.execute(
            "INSERT INTO turni_produzione (data, nome_turno) VALUES (?, ?)",
            (data_t, nome_t)
        )
        turno_id = cursor.lastrowid

        # Recuperiamo gli ID delle macchine
        cursor.execute("SELECT id, tipo FROM macchinari")
        macc_rows = cursor.fetchall()

        for macc in macc_rows:
            macc_id = macc['id']
            tipo_macc = macc['tipo']

            # Generazione dati per tipo di macchina
            if tipo_macc == 'Stampa':
                prodotti = random.randint(450, 600)
                scarti = random.randint(15, 40)       
                kwh = round(random.uniform(25.0, 35.0), 2)
                fermo = random.randint(10, 45)      
            elif tipo_macc == 'Asciugatura':
                prodotti = random.randint(450, 600)
                scarti = random.randint(2, 10)
                kwh = round(random.uniform(70.0, 95.0), 2) 
                fermo = random.randint(5, 20)
            else:  # Imballo
                prodotti = random.randint(430, 580)
                scarti = random.randint(0, 5)
                kwh = round(random.uniform(5.0, 10.0), 2)
                fermo = random.randint(0, 15)

            tempo_operativo = 480 - fermo  

            cursor.execute("""
                INSERT INTO rilevazioni_turno 
                (macchinario_id, turno_id, pezzi_prodotti, pezzi_scarto, consumo_kwh, minuti_fermo, tempo_operativo_minuti)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (macc_id, turno_id, prodotti, scarti, kwh, fermo, tempo_operativo))

    conn.commit()
    conn.close()
    print("Popolamento dati stocastici completato con successo.")

if __name__ == "__main__":
    popola_dati_iniziali()