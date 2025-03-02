import sqlite3
import csv

# Funkcija za uvoz podatkov iz CSV datoteke v bazo
def import_csv(filename, table):
    conn = sqlite3.connect("igre.db")
    cursor = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Preberi glavo CSV
        placeholders = ", ".join("?" * len(header))

        for row in csv_reader:
            cursor.execute(f"INSERT OR IGNORE INTO {table} VALUES ({placeholders})", row)

    conn.commit()
    conn.close()

# Uvoz vseh podatkov iz CSV datotek
# import_csv("video_igre.csv", "video_igre")
# import_csv("izdajatelji.csv", "izdajatelji")
# import_csv("igre_izdajatelj.csv", "igre_izdajatelj")
# import_csv("konzole.csv", "konzole")
# import_csv("igre_konzole.csv", "igre_konzole")
# import_csv("zanri.csv", "zanri")
# import_csv("igre_zanri.csv", "igre_zanri")
# import_csv("ocene.csv", "ocene")