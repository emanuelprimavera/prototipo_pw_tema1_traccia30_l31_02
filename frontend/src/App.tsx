import { useEffect, useState } from "react";
import { getDashboardData } from "./services/api";
import type { KpiGlobali, Macchinario, Rilevazione } from "./types";
import KpiCards from "./components/KpiCards";
import MacchinariTable from "./components/MacchinariTable";
import RilevazioniTable from "./components/RilevazioniTable";
import "./App.css";

function App() {
  const [kpi, setKpi] = useState<KpiGlobali | null>(null);
  const [macchinari, setMacchinari] = useState<Macchinario[]>([]);
  const [rilevazioni, setRilevazioni] = useState<Rilevazione[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        setLoading(true);
        const data = await getDashboardData();

        setKpi(data.kpi);
        setMacchinari(data.macchinari);
        setRilevazioni(data.rilevazioni);
        setError(null);
      } catch (err) {
        console.error("Errore di connessione al back-end:", err);
        setError(
          "Impossibile connettersi al server FastAPI. Verifica che sia avviato.",
        );
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="loading-box">
        <h3>Caricamento dei dati di stabilimento in corso...</h3>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-box">
        <h4>Errore di Sistema</h4>
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="dashboard-container">
      {/* Intestazione */}
      <header className="dashboard-header">
        <h1>📊 Monitoraggio Industria 4.0/5.0 — Laboratorio Serigrafia</h1>
        <p>
          Cruscotto direzionale per il controllo economico-operativo di reparto
          (Corso L-31)
        </p>
      </header>

      {kpi && <KpiCards kpi={kpi} />}
      <MacchinariTable macchinari={macchinari} />
      <RilevazioniTable rilevazioni={rilevazioni} />
    </div>
  );
}

export default App;
