import sqlite3
from datetime import datetime
from modeli import VideoIgra
from modeli import Ocena

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
    detajli = VideoIgra.poisci_igro_z_detajli(iskano)

    if detajli:
        igra = detajli["igra"]
        print(f"\n--- Podrobnosti igre '{igra[1]}' ---")
        print(f"Opis: {igra[2]}")
        print(f"Datum izida: {igra[3]}")
        print(f"Starostna omejitev: {igra[4]}+")
        print(f"Povprečna ocena: {detajli['povprecna_ocena'] or 'Ni ocen'}")

        if detajli['komentarji']:
            print("Komentarji:")
            for komentar in detajli['komentarji']:
                print(f"- {komentar}")
        else:
            print("Ni komentarjev.")
    else:
        print("Igra ni bila najdena.")

def filtriraj_po_zanru():
    ime_zanra = input("Vnesi žanr (točno ime): ")
    igre = VideoIgra.igre_po_zanru(ime_zanra)

    if igre:
        print(f"\n--- Igre v žanru '{ime_zanra}' ---")
        for igra in igre:
            print(f"ID: {igra[0]}, Ime: {igra[1]}, Opis: {igra[2]}")
    else:
        print(f"\nV žanru '{ime_zanra}' ni najdenih iger.")


def dodaj_komentar():
    try:
        igra_id = int(input("Vnesi ID igre: "))
        komentar = input("Vpiši komentar: ")
        ocena = int(input("Vnesi oceno (1-10): "))

        if ocena < 1 or ocena > 10:
            print("Ocena mora biti med 1 in 10.")
            return

        uspesno, sporocilo = Ocena.dodaj_oceno_komentar(igra_id, ocena, komentar)
        print(sporocilo)

    except ValueError:
        print("Napaka: ID in ocena morata biti številki.")
    except Exception as e:
        print("Napaka pri dodajanju komentarja:", e)

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
