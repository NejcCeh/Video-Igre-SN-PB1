import requests
import time
import csv
import random
from datetime import datetime, timedelta

API_KEY = "2dfa9292629a4b89a89169e532c04527"
BASE_URL = "https://api.rawg.io/api/games"

def pridobi_igre_csv(stevilo_iger=200):
    page = 1
    pridobljene_igre = 0
    podatki_csv = []

    while pridobljene_igre < stevilo_iger:
        params = {
            "key": API_KEY,
            "page_size": 40,
            "page": page,
            "ordering": "-rating"
        }

        odgovor = requests.get(BASE_URL, params=params)
        if odgovor.status_code != 200:
            print("Napaka pri pridobivanju strani", page)
            break

        igre = odgovor.json()["results"]
        if not igre:
            break

        for igra in igre:
            if pridobljene_igre >= stevilo_iger:
                break

            ime = igra["name"]
            datum = igra.get("released", "Ni datuma")
            slug = igra["slug"]

            podrobnosti_url = f"https://api.rawg.io/api/games/{slug}?key={API_KEY}"
            podrobnosti_odgovor = requests.get(podrobnosti_url)

            if podrobnosti_odgovor.status_code == 200:
                data = podrobnosti_odgovor.json()
                opis_raw = data.get("description_raw", "Ni opisa").replace("\n", " ").replace("\r", "")
                opis = opis_raw[:297] + "..." if len(opis_raw) > 300 else opis_raw

                esrb = data.get("esrb_rating")
                starost = esrb.get("name") if esrb else "Ni omejitve"
            else:
                opis = "Napaka pri opisu"
                starost = "?"

            vrstica = [pridobljene_igre + 1, ime, opis, starost, datum]
            podatki_csv.append(vrstica)
            pridobljene_igre += 1
            time.sleep(1)

        page += 1

    # Shrani CSV
    with open("video_igre.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id", "ime", "opis", "starostna_omejitev", "datum_izida"])
        writer.writerows(podatki_csv)

    print(f"\n Pridobljenih {pridobljene_igre} iger. CSV datoteka uspešno ustvarjena!")


def pridobi_izdajatelje(stevilo_iger=200):
    page = 1
    igra_id_counter = 1
    izdajatelji = {}
    izdajatelji_data = []
    igre_izdajatelj = []
    izdajatelj_id_counter = 1

    while igra_id_counter <= stevilo_iger:
        params = {
            "key": API_KEY,
            "page_size": 40,
            "page": page,
            "ordering": "-rating"
        }

        odgovor = requests.get(BASE_URL, params=params)
        if odgovor.status_code != 200:
            print(f"Napaka pri pridobivanju strani {page}")
            break

        igre = odgovor.json()["results"]
        if not igre:
            break

        for igra in igre:
            if igra_id_counter > stevilo_iger:
                break

            slug = igra["slug"]
            podrobnosti_url = f"https://api.rawg.io/api/games/{slug}?key={API_KEY}"
            podrobnosti_odgovor = requests.get(podrobnosti_url)

            if podrobnosti_odgovor.status_code == 200:
                data = podrobnosti_odgovor.json()
                publishers = data.get("publishers", [])
                if not publishers:
                    publishers = data.get("developers", [])  # nadomestni vir


                for pub in publishers:
                    ime = pub["name"]
                    spletna = pub.get("website", "Ni podatka")

                    if ime not in izdajatelji:
                        izdajatelji[ime] = izdajatelj_id_counter
                        izdajatelji_data.append([
                            izdajatelj_id_counter,
                            ime,
                            "???",  # država ni podana
                            "???",  # leto ustanovitve ni podano
                            spletna
                        ])
                        izdajatelj_id_counter += 1

                    igre_izdajatelj.append([
                        igra_id_counter,
                        izdajatelji[ime]
                    ])
            else:
                print(f"Napaka pri podrobnostih igre {slug}")

            igra_id_counter += 1
            time.sleep(1)

        page += 1

    # Shrani .csv datoteke
    with open("izdajatelji.csv", "w", encoding="utf-8", newline="") as f1:
        writer = csv.writer(f1)
        writer.writerow(["id", "ime", "drzava", "leto_ustanovitve", "spletna_stran"])
        writer.writerows(izdajatelji_data)

    with open("igre_izdajatelj.csv", "w", encoding="utf-8", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(["igra_id", "izdajatelj_id"])
        writer.writerows(igre_izdajatelj)

    print(f"\n Izdajatelji in povezave so uspešno zapisani za {igra_id_counter - 1} iger.")


def pridobi_konzole_in_povezave(stevilo_iger=200):
    page = 1
    igra_id_counter = 1
    konzole = {}
    konzole_data = []
    igre_konzole = []
    konzola_id_counter = 1

    while igra_id_counter <= stevilo_iger:
        params = {
            "key": API_KEY,
            "page_size": 40,
            "page": page,
            "ordering": "-rating"
        }

        odgovor = requests.get(BASE_URL, params=params)
        if odgovor.status_code != 200:
            print(f"Napaka pri pridobivanju strani {page}")
            break

        igre = odgovor.json()["results"]
        if not igre:
            break

        for igra in igre:
            if igra_id_counter > stevilo_iger:
                break

            slug = igra["slug"]
            podrobnosti_url = f"https://api.rawg.io/api/games/{slug}?key={API_KEY}"
            odgovor_podrobnosti = requests.get(podrobnosti_url)

            if odgovor_podrobnosti.status_code == 200:
                data = odgovor_podrobnosti.json()
                platforms = data.get("platforms", [])

                for entry in platforms:
                    platform_name = entry["platform"]["name"]

                    if platform_name not in konzole:
                        konzole[platform_name] = konzola_id_counter
                        konzole_data.append([konzola_id_counter, platform_name])
                        konzola_id_counter += 1

                    igre_konzole.append([igra_id_counter, konzole[platform_name]])

            else:
                print(f"Napaka pri podrobnostih igre {slug}")

            igra_id_counter += 1
            time.sleep(1)

        page += 1

    # Shrani konzole
    with open("konzole.csv", "w", encoding="utf-8", newline="") as f1:
        writer = csv.writer(f1)
        writer.writerow(["id", "ime"])
        writer.writerows(konzole_data)

    # Shrani povezovalno tabelo
    with open("igre_konzole.csv", "w", encoding="utf-8", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(["igra_id", "konzola_id"])
        writer.writerows(igre_konzole)

    print(f"\n Končano! Povezave zapisane za {igra_id_counter - 1} iger. Skupaj {len(konzole)} konzol.")


def pridobi_zanre_in_povezave(stevilo_iger=200):
    page = 1
    igra_id_counter = 1
    zanri = {}
    zanri_data = []
    igre_zanri = []
    zanr_id_counter = 1

    while igra_id_counter <= stevilo_iger:
        params = {
            "key": API_KEY,
            "page_size": 40,
            "page": page,
            "ordering": "-rating"
        }

        odgovor = requests.get(BASE_URL, params=params)
        if odgovor.status_code != 200:
            print(f"Napaka pri pridobivanju strani {page}")
            break

        igre = odgovor.json()["results"]
        if not igre:
            break

        for igra in igre:
            if igra_id_counter > stevilo_iger:
                break

            slug = igra["slug"]
            podrobnosti_url = f"https://api.rawg.io/api/games/{slug}?key={API_KEY}"
            odgovor_podrobnosti = requests.get(podrobnosti_url)

            if odgovor_podrobnosti.status_code == 200:
                data = odgovor_podrobnosti.json()
                genres = data.get("genres", [])

                for genre in genres:
                    ime_zanra = genre["name"]

                    if ime_zanra not in zanri:
                        zanri[ime_zanra] = zanr_id_counter
                        zanri_data.append([zanr_id_counter, ime_zanra])
                        zanr_id_counter += 1

                    igre_zanri.append([igra_id_counter, zanri[ime_zanra]])

            else:
                print(f"Napaka pri podrobnostih igre {slug}")

            igra_id_counter += 1
            time.sleep(1)

        page += 1

    # Shrani žanre
    with open("zanri.csv", "w", encoding="utf-8", newline="") as f1:
        writer = csv.writer(f1)
        writer.writerow(["id", "ime"])
        writer.writerows(zanri_data)

    # Shrani povezovalno tabelo
    with open("igre_zanri.csv", "w", encoding="utf-8", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(["igra_id", "zanr_id"])
        writer.writerows(igre_zanri)

    print(f"\n Pridobljenih {igra_id_counter - 1} iger in {len(zanri)} žanrov. CSV datoteke ustvarjene!")




def generiraj_ocene(datoteka="ocene.csv"):
    """Naljučno generirane ocene"""
    stevilo_iger = 200
    max_ocen_na_igro = 5
    komentarji = [
        "Izjemna avantura s čudovito grafiko",
        "Zelo dober gameplay, a manjka globine",
        "Epsko doživetje – priporočam!",
        "Igra ima potencial, a je hroščata",
        "Fantastična zgodba, popoln zaključek",
        "Zabavno za več igralcev",
        "Noro dobra akcija, brez premora!",
        "Igralno lepo uravnotežena",
        "Zabavna, čeprav nekoliko kratka",
        "Temna, a zelo zadovoljiva izkušnja",
        "Dober ambient in močan soundtrack",
        "Vrhunska fizika in svoboda",
        "Preveč ponavljajoče, hitro postane dolgočasno",
        "Odlična glasba in občutek igranja",
        "Pogrešam boljšo optimizacijo",
        "Zelo dobra za ljubitelje simulacij",
        "Mojstrovina! Igral bom še večkrat",
        "Težko, a pošteno!",
        "Ni izstopalo",
        "Adrenalinska vožnja kot nobena druga"
    ]
    ocene_data = []
    ocena_id = 1
    zacetni_datum = datetime(2024, 1, 1)

    for igra_id in range(1, stevilo_iger + 1):
        stevilo_ocen = random.randint(1, max_ocen_na_igro)
        for _ in range(stevilo_ocen):
            ocena = random.randint(6, 10)
            komentar = random.choice(komentarji)
            nakljucni_dan = random.randint(0, 300)
            datum = zacetni_datum + timedelta(days=nakljucni_dan)
            datum_str = datum.strftime("%Y-%m-%d")
            ocene_data.append([ocena_id, igra_id, ocena, komentar, datum_str])
            ocena_id += 1

    with open("ocene.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "igra_id", "ocena", "komentar", "datum_ocene"])
        writer.writerows(ocene_data)

    print(f"Uspešno ustvarjenih {len(ocene_data)} ocen za {stevilo_iger} iger. Shranjeno v '{datoteka}'.")


#pridobi_igre_csv()
#pridobi_izdajatelje()
#pridobi_konzole_in_povezave()
#pridobi_zanre_in_povezave()
#generiraj_ocene()

