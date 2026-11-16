import type { Rilevazione } from '../types';

interface RilevazioniTableProps {
  rilevazioni: Rilevazione[];
}

function RilevazioniTable({ rilevazioni }: RilevazioniTableProps) {
  return (
    <div className="section-card">
      <div className="section-header">
        Registro Storico Rilevazioni per Turno
      </div>
      <div className="table-responsive">
        <table className="custom-table">
          <thead>
            <tr>
              <th>Data</th>
              <th>Turno</th>
              <th>Macchinario</th>
              <th>Prodotti</th>
              <th>Scarti</th>
              <th>Consumo (kWh)</th>
              <th>Minuti Fermo</th>
            </tr>
          </thead>
          <tbody>
            {rilevazioni.map((rilevazione) => (
              <tr key={rilevazione.id}>
                <td>{rilevazione.data}</td>
                <td>{rilevazione.nome_turno}</td>
                <td><strong>{rilevazione.nome_macchina}</strong></td>
                <td>{rilevazione.pezzi_prodotti}</td>
                <td>
                  <span style={{ color: '#dc3545', fontWeight: 'bold' }}>
                    {rilevazione.pezzi_scarto}
                  </span>
                </td>
                <td>{rilevazione.consumo_kwh}</td>
                <td>
                  <span className="badge warning">
                    {rilevazione.minuti_fermo} min
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default RilevazioniTable;
