import type { Macchinario } from '../types';

interface MacchinariTableProps {
  macchinari: Macchinario[];
}

function MacchinariTable({ macchinari }: MacchinariTableProps) {
  return (
    <div className="section-card">
      <div className="section-header">
        Stazioni di Lavoro Monitorate (Anagrafica)
      </div>
      <div className="table-responsive">
        <table className="custom-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome Macchina</th>
              <th>Tipologia</th>
              <th>Costo Orario Fermo (€/h)</th>
            </tr>
          </thead>
          <tbody>
            {macchinari.map((macchinario) => (
              <tr key={macchinario.id}>
                <td>{macchinario.id}</td>
                <td><strong>{macchinario.nome_macchina}</strong></td>
                <td><span className="badge">{macchinario.tipo}</span></td>
                <td>€ {macchinario.costo_orario_fermo.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default MacchinariTable;
