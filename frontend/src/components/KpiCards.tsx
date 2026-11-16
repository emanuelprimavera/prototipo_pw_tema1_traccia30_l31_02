import type { KpiGlobali } from '../types';

interface KpiCardsProps {
  kpi: KpiGlobali;
}

function KpiCards({ kpi }: KpiCardsProps) {
  return (
    <div className="kpi-grid">
      <div className="kpi-card">
        <h6>Pezzi Totali Prodotti</h6>
        <h2>{kpi.totale_pezzi_prodotti}</h2>
        <small>Conforme agli standard</small>
      </div>

      <div className="kpi-card danger">
        <h6>Tasso di Scarto</h6>
        <h2>{kpi.tasso_scarto_percentuale}%</h2>
        <small>Perdita: € {kpi.impatto_finanziario_scarti_eur}</small>
      </div>

      <div className="kpi-card warning">
        <h6>Costo Fermi Macchina</h6>
        <h2>€ {kpi.costo_totale_fermi_macchina_eur}</h2>
        <small>Inattività di reparto</small>
      </div>

      <div className="kpi-card success">
        <h6>Consumo Energetico</h6>
        <h2>{kpi.consumo_energetico_totale_kwh} kWh</h2>
        <small>Costo: € {kpi.costo_totale_energia_eur}</small>
      </div>
    </div>
  );
}

export default KpiCards;
