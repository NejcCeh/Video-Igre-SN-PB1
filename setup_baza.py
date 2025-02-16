import sqlite3

# Povežemo se (ali ustvarimo) bazo SQLite
conn = sqlite3.connect("igre.db")
cursor = conn.cursor()

# Ustvarimo tabelo video_igre
cursor.execute("""
CREATE TABLE IF NOT EXISTS video_igre (
    id INTEGER PRIMARY KEY,
    ime TEXT NOT NULL,
    tekstovni_opis TEXT,
    starostna_omejitev INTEGER,
    datum_izida TEXT
);
""")

# Ustvarimo tabelo izdajatelji
cursor.execute("""
CREATE TABLE IF NOT EXISTS izdajatelji (
    id INTEGER PRIMARY KEY,
    ime TEXT NOT NULL,
    država TEXT,
    leto_ustanovitve INTEGER,
    spletna_stran TEXT
);
""")

# Ustvarimo tabelo povezava igre - izdajatelj (1:N)
cursor.execute("""
CREATE TABLE IF NOT EXISTS igre_izdajatelj (
    id_igre INTEGER,
    id_izdajatelja INTEGER,
    FOREIGN KEY (id_igre) REFERENCES video_igre(id),
    FOREIGN KEY (id_izdajatelja) REFERENCES izdajatelji(id)
);
""")

# Ustvarimo tabelo konzole
cursor.execute("""
CREATE TABLE IF NOT EXISTS konzole (
    id INTEGER PRIMARY KEY,
    ime TEXT NOT NULL,
    datum_izida TEXT,
    proizvajalec TEXT,
    generacija TEXT
);
""")

# Ustvarimo tabelo povezava igre - konzole (N:N)
cursor.execute("""
CREATE TABLE IF NOT EXISTS igre_konzole (
    id_igre INTEGER,
    id_konzole INTEGER,
    FOREIGN KEY (id_igre) REFERENCES video_igre(id),
    FOREIGN KEY (id_konzole) REFERENCES konzole(id)
);
""")

# Potrdimo spremembe in zapremo povezavo
conn.commit()
conn.close()

