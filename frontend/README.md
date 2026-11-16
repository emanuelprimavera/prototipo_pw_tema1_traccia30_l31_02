# Monitoraggio Industria 4.0/5.0

Istruzioni per avviare il back-end (BE) e il front-end (FE) in locale. Sono
necessari Python 3, Node.js e npm.

## Back-end

Apri un terminale nella cartella `backend`:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Il server FastAPI sarà disponibile su <http://127.0.0.1:8000>. La documentazione
interattiva delle API è disponibile su <http://127.0.0.1:8000/docs>.

Lascia questo terminale aperto mentre usi l'applicazione. Per fermare il server,
premi `Ctrl+C`; per uscire dall'ambiente virtuale, esegui `deactivate`.

### Database

Il back-end cerca `database.db` nella directory corrente: avvia quindi Uvicorn
dalla cartella `backend`, come nei comandi sopra.

Se il database non esiste, puoi creare le tabelle con:

```bash
python database.py
```

Per inserire dati dimostrativi:

```bash
python generatore_dati.py
```

**Attenzione:** il generatore elimina le rilevazioni e i turni esistenti prima
di crearne di nuovi. Non eseguirlo se vuoi conservare i dati attuali.

## Front-end

Apri un secondo terminale nella cartella `frontend`:

```bash
cd frontend
npm install
npm run dev
```

Apri nel browser l'indirizzo mostrato da Vite, normalmente
<http://localhost:5173>. Il front-end richiede che il back-end sia già avviato
su <http://127.0.0.1:8000>.

Per fermare il server di sviluppo, premi `Ctrl+C` nel relativo terminale.

## Avvii successivi

Dopo la prima installazione delle dipendenze, per riavviare il progetto basta
aprire due terminali:

1. Nella cartella `backend`, attiva l'ambiente virtuale ed esegui Uvicorn:
   `source .venv/bin/activate` e `uvicorn main:app --reload`.
2. Nella cartella `frontend`, esegui `npm run dev`.
