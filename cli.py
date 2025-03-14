import sqlite3
from datetime import datetime

def povezava_z_bazo():
    return sqlite3.connect("igre.db")

def prikazi_meni():
    print("\n=== VIDEO IGRE - TEKSTOVNI VMESNIK ===")
    print("1. Prikaži vse igre")
    print("2. Išči igro po imenu")
    print("3. Filtriraj igre po žanru")
    print("4. Dodaj komentar k igri")
    print("5. Izhod")
    return input("Izberi možnost (1-5): ")

def prikazi_igre():
    conn = povezava_z_bazo()
    c = conn.cursor()
    c.execute("SELECT id, ime FROM video_igre ORDER BY id ASC")
    igre = c.fetchall()
    print("\n--- Seznam vseh iger ---")
    for igra in igre:
        print(f"{igra[0]}: {igra[1]}")
    conn.close()

def poisci_igro():
    iskano = input("Vnesi ime igre: ")
    conn = povezava_z_bazo()
    c = conn.cursor()
    c.execute("SELECT * FROM video_igre WHERE ime LIKE ?", ('%' + iskano + '%',))
    igra = c.fetchone()

    if igra:
        print(f"\n--- Podrobnosti igre '{igra[1]}' ---")
        print(f"Opis: {igra[2]}")
        print(f"Datum izida: {igra[3]}")
        print(f"Starostna omejitev: {igra[4]}+")

        # Povprečna ocena
        c.execute("SELECT AVG(ocena) FROM ocene WHERE igra_id = ?", (igra[0],))
        povp = c.fetchone()[0]
        print(f"Povprečna ocena: {round(povp, 2) if povp else 'Ni ocen'}")

        # Komentarji
        # Komentarji (maks 5)
        c.execute("SELECT komentar FROM ocene WHERE igra_id = ? AND komentar IS NOT NULL LIMIT 5", (igra[0],))
        komentarji = c.fetchall()  

        if komentarji:
            print("Komentarji:")
            for komentar in komentarji:
                print(f"- {komentar[0]}")
        else:
            print("Ni komentarjev.")
    else:
        print("Igra ni bila najdena.")
    conn.close()

def filtriraj_po_zanru():
    ime_zanra = input("Vnesi žanr (točno ime): ")
    conn = sqlite3.connect("igre.db")
    c = conn.cursor()

    c.execute("""
        SELECT vi.id, vi.ime, vi.opis
        FROM video_igre vi
        JOIN igre_zanri iz ON vi.id = iz.igra_id
        JOIN zanri z ON iz.zanr_id = z.id
        WHERE z.naziv = ?
        ORDER BY vi.id
    """, (ime_zanra,))

    igre = c.fetchall()
    conn.close()

    if igre:
        print(f"\n--- Igre v žanru '{ime_zanra}' ---")
        for igra in igre:
            print(f"ID: {igra[0]}, Ime: {igra[1]}, Opis: {igra[2]}")
    else:
        print(f"\nV žanru '{ime_zanra}' ni najdenih iger.")


def dodaj_komentar():
    conn = sqlite3.connect("igre.db")
    c = conn.cursor()

    try:
        igra_id = int(input("Vnesi ID igre: "))
        komentar = input("Vpiši komentar: ")
        ocena = int(input("Vnesi oceno (1-10): "))

        if ocena < 1 or ocena > 10:
            print("Ocena mora biti med 1 in 10.")
            return

        datum = datetime.now().strftime("%Y-%m-%d")

        c.execute("SELECT * FROM video_igre WHERE id = ?", (igra_id,))
        if not c.fetchone():
            print("Igra z ID-jem ne obstaja.")
            return

        c.execute("""
            INSERT INTO ocene (igra_id, ocena, komentar, datum_ocene)
            VALUES (?, ?, ?, ?)
        """, (igra_id, ocena, komentar, datum))
        
        conn.commit()
        print("Komentar uspešno dodan.")
    except Exception as e:
        print("Napaka pri dodajanju komentarja:", e)
    finally:
        conn.close()

def main():
    while True:
        izbira = prikazi_meni()
        if izbira == "1":
            prikazi_igre()
        elif izbira == "2":
            poisci_igro()
        elif izbira == "3":
            filtriraj_po_zanru()
        elif izbira == "4":
            dodaj_komentar()
        elif izbira == "5":
            print("Izhod. Hvala za uporabo.")
            break
        else:
            print("Neveljavna izbira. Poskusi znova.")

if __name__ == "__main__":
    main()
