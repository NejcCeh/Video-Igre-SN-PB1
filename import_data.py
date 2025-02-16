import sqlite3
import csv

# Povezava z SQLite bazo
conn = sqlite3.connect("igre.db")
cursor = conn.cursor()

# Funkcija za uvoz podatkov iz CSV
def import_csv(file, table):
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Preskoči glavo CSV
        for row in reader:
            placeholders = ", ".join(["?"] * len(row))
            cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", row)

# Uvoz podatkov
import_csv("video_igre.csv", "video_igre")
import_csv("izdajatelji.csv", "izdajatelji")
import_csv("igre_izdajatelj.csv", "igre_izdajatelj")
import_csv("konzole.csv", "konzole")
import_csv("igre_konzole.csv", "igre_konzole")


conn.commit()
conn.close()


