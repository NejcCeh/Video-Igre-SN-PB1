import sqlite3

# Funkcija za ustvarjanje tabel v bazi
def create_tables():
    conn = sqlite3.connect("igre.db")
    cursor = conn.cursor()

    cursor.executescript("""
        PRAGMA foreign_keys = ON;

        CREATE TABLE IF NOT EXISTS video_igre (
            id INTEGER PRIMARY KEY,
            ime TEXT NOT NULL UNIQUE,
            opis TEXT,
            starostna_omejitev TEXT,
            datum_izida TEXT
        );

        CREATE TABLE IF NOT EXISTS izdajatelji (
            id INTEGER PRIMARY KEY,
            ime TEXT NOT NULL,
            drzava TEXT,
            leto_ustanovitve INTEGER,
            spletna_stran TEXT
        );

        CREATE TABLE IF NOT EXISTS igre_izdajatelj (
            igra_id INTEGER,
            izdajatelj_id INTEGER,
            PRIMARY KEY (igra_id, izdajatelj_id),
            FOREIGN KEY (igra_id) REFERENCES video_igre(id) ON DELETE CASCADE,
            FOREIGN KEY (izdajatelj_id) REFERENCES izdajatelji(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS konzole (
            id INTEGER PRIMARY KEY,
            ime TEXT NOT NULL,
            datum_izida TEXT,
            proizvajalec TEXT,
            generacija INTEGER
        );

        CREATE TABLE IF NOT EXISTS igre_konzole (
            igra_id INTEGER,
            konzola_id INTEGER,
            PRIMARY KEY (igra_id, konzola_id),
            FOREIGN KEY (igra_id) REFERENCES video_igre(id) ON DELETE CASCADE,
            FOREIGN KEY (konzola_id) REFERENCES konzole(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS zanri (
            id INTEGER PRIMARY KEY,
            naziv TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS igre_zanri (
            igra_id INTEGER,
            zanr_id INTEGER,
            PRIMARY KEY (igra_id, zanr_id),
            FOREIGN KEY (igra_id) REFERENCES video_igre(id) ON DELETE CASCADE,
            FOREIGN KEY (zanr_id) REFERENCES zanri(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS ocene (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            igra_id INTEGER,
            ocena INTEGER CHECK(ocena BETWEEN 1 AND 10),
            komentar TEXT,
            datum_ocene TEXT,
            FOREIGN KEY (igra_id) REFERENCES video_igre(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()

create_tables()