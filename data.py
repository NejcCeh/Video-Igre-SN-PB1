import csv

# Ustvari CSV datoteko
def create_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Seznam za video igre
video_igre_data = [
    ["id", "ime", "opis", "starostna_omejitev", "datum_izida"],
    [1, "The Witcher 3", "Open-world RPG", 18, "2015-05-19"],
    [2, "GTA V", "Action-adventure", 18, "2013-09-17"],
    [3, "Minecraft", "Sandbox", 7, "2011-11-18"]
]

# Seznam za izdajatelje
izdajatelji_data = [
    ["id", "ime", "drzava", "leto_ustanovitve", "spletna_stran"],
    [1, "CD Projekt Red", "Poljska", 2002, "https://www.cdprojektred.com"],
    [2, "Rockstar Games", "ZDA", 1998, "https://www.rockstargames.com"],
    [3, "Mojang Studios", "Švedska", 2009, "https://www.minecraft.net"]
]

# Seznam za povezave igre ↔ izdajatelj
igre_izdajatelj_data = [
    ["igra_id", "izdajatelj_id"],
    [1, 1],
    [2, 2],
    [3, 3]
]

# Seznam za konzole
konzole_data = [
    ["id", "ime", "datum_izida", "proizvajalec", "generacija"],
    [1, "PC", "N/A", "Various", "N/A"],
    [2, "PlayStation 4", "2013-11-15", "Sony", 8],
    [3, "Xbox One", "2013-11-22", "Microsoft", 8]
]

# Seznam za povezave igre ↔ konzola
igre_konzole_data = [
    ["igra_id", "konzola_id"],
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [2, 3],
    [3, 1],
    [3, 2]
]

# Seznam za žanre
zanri_data = [
    ["id", "naziv"],
    [1, "RPG"],
    [2, "Action"],
    [3, "Sandbox"]
]

# Seznam za povezave igre ↔ žanri
igre_zanri_data = [
    ["igra_id", "zanr_id"],
    [1, 1],
    [2, 2],
    [3, 3]
]

# Seznam za ocene
ocene_data = [
    ["id", "igra_id", "ocena", "komentar", "datum_ocene"],
    [1, 1, 10, "Fantastična igra!", "2024-02-01"],
    [2, 2, 9, "Igra z odličnim zgodbo!", "2024-02-02"],
    [3, 3, 8, "Zelo kreativna igra", "2024-02-03"]
]

# Ustvari vse CSV datoteke
create_csv("video_igre.csv", video_igre_data)
create_csv("izdajatelji.csv", izdajatelji_data)
create_csv("igre_izdajatelj.csv", igre_izdajatelj_data)
create_csv("konzole.csv", konzole_data)
create_csv("igre_konzole.csv", igre_konzole_data)
create_csv("zanri.csv", zanri_data)
create_csv("igre_zanri.csv", igre_zanri_data)
create_csv("ocene.csv", ocene_data)

