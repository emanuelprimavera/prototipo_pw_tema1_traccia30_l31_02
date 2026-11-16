export interface KpiGlobali {
  totale_pezzi_prodotti: number;
  tasso_scarto_percentuale: number;
  impatto_finanziario_scarti_eur: number;
  costo_totale_fermi_macchina_eur: number;
  consumo_energetico_totale_kwh: number;
  costo_totale_energia_eur: number;
}

export interface Macchinario {
  id: number;
  nome_macchina: string;
  tipo: string;
  costo_orario_fermo: number;
}

export interface Rilevazione {
  id: number;
  data: string;
  nome_turno: string;
  nome_macchina: string;
  pezzi_prodotti: number;
  pezzi_scarto: number;
  consumo_kwh: number;
  minuti_fermo: number;
}
