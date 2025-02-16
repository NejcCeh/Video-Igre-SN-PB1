import csv

# Ustvari CSV datoteko
def create_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Podatki za video igre
video_igre = [
    ["id", "ime", "tekstovni_opis", "starostna_omejitev", "datum_izida"],
    [1, "CyberWar 2077", "Futuristična RPG igra v odprtem svetu.", 18, "2020-12-10"],
    [2, "Shadow Quest", "Temna fantazijska avantura s taktičnimi boji.", 16, "2019-05-15"],
    [3, "Pixel Racer", "Retro 2D dirkalna igra z arkadnim občutkom.", 3, "2021-07-22"],
    [4, "Zombie Apocalypse X", "Preživetvena horror igra z zombiji.", 18, "2018-10-31"],
    [5, "Galactic Battles", "Strategija v vesolju s spektakularnimi bitkami.", 12, "2022-03-14"],
    [6, "Fantasy Kingdoms", "MMORPG v svetu magije in mitov.", 16, "2020-09-07"],
    [7, "Speed Legends", "Simulacija vožnje z realističnimi avtomobili.", 3, "2021-11-20"],
    [8, "Magic Duel", "Kartaška igra s čarobnimi bitji in uroki.", 7, "2019-06-30"],
    [9, "Warzone Tactical", "Vojaška strelska igra z realističnimi misijami.", 18, "2023-01-18"],
    [10, "Underground Hacker", "Simulacija hekanja in programiranja.", 12, "2022-05-25"],
]

# Podatki za izdajatelje
izdajatelji = [
    ["id", "ime", "država", "leto_ustanovitve", "spletna_stran"],
    [1, "GameStudioX", "ZDA", 2005, "https://gamestudiox.com"],
    [2, "Retro Games Inc.", "Japonska", 1990, "https://retrogames.jp"],
    [3, "DarkPixel Studios", "Nemčija", 2015, "https://darkpixel.de"],
    [4, "FantasyWorks", "Francija", 2012, "https://fantasyworks.fr"],
]

# Povezava igre - izdajatelji (1:N)
igre_izdajatelj = [
    ["id_igre", "id_izdajatelja"],
    [1, 1],
    [2, 3],
    [3, 2],
    [4, 3],
    [5, 4],
    [6, 4],
    [7, 2],
    [8, 4],
    [9, 1],
    [10, 3],
]

# Podatki za konzole
konzole = [
    ["id", "ime", "datum_izida", "proizvajalec", "generacija"],
    [1, "PlayStation 5", "2020-11-12", "Sony", "9"],
    [2, "Xbox Series X", "2020-11-10", "Microsoft", "9"],
    [3, "PC", "n/a", "Več proizvajalcev", "Različne"],
    [4, "Nintendo Switch", "2017-03-03", "Nintendo", "8"],
]

# Povezava igre - konzole (N:N)
igre_konzole = [
    ["id_igre", "id_konzole"],
    [1, 1],
    [1, 2],
    [1, 3],
    [2, 1],
    [2, 3],
    [3, 3],
    [4, 2],
    [4, 3],
    [5, 3],
    [5, 4],
    [6, 3],
    [7, 1],
    [7, 2],
    [8, 4],
    [9, 1],
    [9, 2],
    [9, 3],
    [10, 3],
]

# Ustvari vse CSV datoteke
create_csv("video_igre.csv", video_igre)
create_csv("izdajatelji.csv", izdajatelji)
create_csv("igre_izdajatelj.csv", igre_izdajatelj)
create_csv("konzole.csv", konzole)
create_csv("igre_konzole.csv", igre_konzole)


