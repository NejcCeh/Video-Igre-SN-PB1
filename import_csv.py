import sqlite3
import csv

def import_csv(filename, table):
    # Poveži se na bazo
    conn = sqlite3.connect("igre.db")
    cursor = conn.cursor()

    # Odpri CSV datoteko
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Preberi prvi vrstico (glavo)
        
        # Pripravi poizvedbo za vstavljanje podatkov
        placeholders = ", ".join("?" * len(header))
        for row in csv_reader:
            cursor.execute(f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})", row)
    conn.commit()
    conn.close()

# Uvoz podatkov
import_csv("video_igre.csv", "video_igre")
import_csv("izdajatelji.csv", "izdajatelji")
import_csv("igre_izdajatelj.csv", "igre_izdajatelj")
import_csv("konzole.csv", "konzole")
import_csv("igre_konzole.csv", "igre_konzole")

# Potrdimo spremembe in zapremo povezavo


