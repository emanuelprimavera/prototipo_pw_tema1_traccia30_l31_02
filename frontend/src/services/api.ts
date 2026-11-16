import axios from 'axios';
import type { KpiGlobali, Macchinario, Rilevazione } from '../types';

const API_BASE_URL = 'http://127.0.0.1:8000';

export async function getDashboardData() {
  const [kpi, macchinari, rilevazioni] = await Promise.all([
    axios.get<KpiGlobali>(`${API_BASE_URL}/api/kpi-globali`),
    axios.get<Macchinario[]>(`${API_BASE_URL}/api/macchinari`),
    axios.get<Rilevazione[]>(`${API_BASE_URL}/api/rilevazioni`)
  ]);

  return {
    kpi: kpi.data,
    macchinari: macchinari.data,
    rilevazioni: rilevazioni.data
  };
}
