# Guida all'avvio dell'applicativo

## 1. Backend

Nel primo terminale, creare e attivare un ambiente virtuale Python, installare le dipendenze e avviare il server:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python generatore_dati.py
uvicorn main:app --reload
```

Il generatore inizializza il database SQLite, inserisce i parametri e i macchinari dimostrativi e crea turni e rilevazioni di esempio. L'API è quindi disponibile all'indirizzo:

```text
http://127.0.0.1:8000
```

La documentazione interattiva degli endpoint FastAPI è disponibile su:

```text
http://127.0.0.1:8000/docs
```

Lasciare questo terminale aperto mentre si usa l'applicazione. Per arrestare il backend, premere `Ctrl+C`.

## 2. Frontend

Aprire un secondo terminale nella cartella principale del progetto e avviare Vite:

```bash
cd frontend
npm install
npm run dev
```

Il terminale mostrerà l'indirizzo locale del frontend, normalmente:

```text
http://localhost:5173
```

Aprire l'indirizzo nel browser. Il frontend invia le richieste API a `http://127.0.0.1:8000`, quindi il backend deve essere già avviato. Lasciare aperto anche questo terminale durante l'utilizzo.
