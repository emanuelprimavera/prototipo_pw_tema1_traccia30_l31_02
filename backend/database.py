import sqlite3
import os

DB_NAME = "database.db"

def get_connection():
    """Crea e restituisce una connessione al database SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def inizializza_database():
    """Crea le tabelle del database se non esistono già."""
    conn = get_connection()
    cursor = conn.cursor()

    # Macchinari
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS macchinari (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_macchina TEXT NOT NULL,
        tipo TEXT NOT NULL,
        costo_orario_fermo REAL NOT NULL
    )
    """)

    # Turni di Produzione
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turni_produzione (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        nome_turno TEXT NOT NULL
    )
    """)

    # Parametri Economici Globali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS costi_parametri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chiave TEXT UNIQUE NOT NULL,
        valore REAL NOT NULL,
        descrizione TEXT
    )
    """)

    # Rilevazioni di Turno (Log Transazionale)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rilevazioni_turno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        macchinario_id INTEGER NOT NULL,
        turno_id INTEGER NOT NULL,
        pezzi_prodotti INTEGER NOT NULL,
        pezzi_scarto INTEGER NOT NULL,
        consumo_kwh REAL NOT NULL,
        minuti_fermo INTEGER NOT NULL,
        tempo_operativo_minuti INTEGER NOT NULL,
        FOREIGN KEY (macchinario_id) REFERENCES macchinari(id),
        FOREIGN KEY (turno_id) REFERENCES turni_produzione(id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database SQLite inizializzato con successo.")

if __name__ == "__main__":
    inizializza_database()