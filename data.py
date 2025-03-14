import csv

# Ustvari CSV datoteko
def create_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Seznam za igre
video_igre_data = [
    ["id", "ime", "opis", "starostna_omejitev", "datum_izida"],
    [1, "The Witcher 3", "Open-world RPG", 18, "2015-05-19"],
    [2, "GTA V", "Action-adventure", 18, "2013-09-17"],
    [3, "Minecraft", "Sandbox", 7, "2011-11-18"],
    [4, "Forza Horizon 5", "Racing game with open-world", 3, "2021-11-09"],
    [5, "Cyberpunk 2077", "Futuristic open-world RPG", 18, "2020-12-10"],
    [6, "Red Dead Redemption 2", "Western action-adventure", 18, "2018-10-26"],
    [7, "Halo Infinite", "Sci-fi FPS", 16, "2021-12-08"],
    [8, "The Legend of Zelda: Breath of the Wild", "Open-world adventure", 12, "2017-03-03"],
    [9, "Super Mario Odyssey", "3D platformer", 3, "2017-10-27"],
    [10, "Dark Souls III", "Hardcore action RPG", 16, "2016-03-24"]
]

# Seznam za izdajatelje
izdajatelji_data = [
    ["id", "ime", "drzava", "leto_ustanovitve", "spletna_stran"],
    [1, "CD Projekt Red", "Poljska", 2002, "https://www.cdprojektred.com"],
    [2, "Rockstar Games", "ZDA", 1998, "https://www.rockstargames.com"],
    [3, "Mojang Studios", "Švedska", 2009, "https://www.minecraft.net"],
    [4, "Playground Games", "Velika Britanija", 2010, "https://playground-games.com"],
    [5, "Bungie", "ZDA", 1991, "https://www.bungie.net"],
    [6, "Nintendo", "Japonska", 1889, "https://www.nintendo.com"],
    [7, "FromSoftware", "Japonska", 1986, "https://www.fromsoftware.jp"]
]

# Seznam za povezave igre - izdajatelj
igre_izdajatelj_data = [
    ["igra_id", "izdajatelj_id"],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 1],
    [6, 2],
    [7, 5],
    [8, 6],
    [9, 6],
    [10, 7]
]

# Seznam za konzole
konzole_data = [
    ["id", "ime", "datum_izida", "proizvajalec", "generacija"],
    [1, "PC", "N/A", "Various", "N/A"],
    [2, "PlayStation 4", "2013-11-15", "Sony", 8],
    [3, "Xbox One", "2013-11-22", "Microsoft", 8],
    [4, "PlayStation 5", "2020-11-12", "Sony", 9],
    [5, "Xbox Series X", "2020-11-10", "Microsoft", 9],
    [6, "Nintendo Switch", "2017-03-03", "Nintendo", 9]
]

# Seznam za povezave igre - konzola
igre_konzole_data = [
    ["igra_id", "konzola_id"],
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [2, 3],
    [3, 1],
    [3, 2],
    [4, 1],
    [4, 3],
    [4, 5],
    [5, 1],
    [5, 4],
    [5, 5],
    [6, 1],
    [6, 2],
    [6, 3],
    [7, 1],
    [7, 3],
    [7, 5],
    [8, 6],
    [9, 6],
    [10, 1],
    [10, 2],
    [10, 3],
    [10, 4]
]

# Seznam za žanre
zanri_data = [
    ["id", "naziv"],
    [1, "RPG"],
    [2, "Action"],
    [3, "Sandbox"],
    [4, "Racing"],
    [5, "FPS"],
    [6, "Adventure"],
    [7, "Platformer"]
]

# Seznam za povezave igre ↔ žanri
igre_zanri_data = [
    ["igra_id", "zanr_id"],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 1],
    [5, 2],
    [6, 2],
    [6, 6],
    [7, 2],
    [7, 5],
    [8, 6],
    [9, 7],
    [10, 1],
    [10, 2]
]

# Seznam za ocene
ocene_data = [
    ["id", "igra_id", "ocena", "komentar", "datum_ocene"],
    [1, 1, 10, "Fantastična igra!", "2024-02-01"],
    [2, 2, 9, "Igra z odličnim zgodbo!", "2024-02-02"],
    [3, 3, 8, "Zelo kreativna igra", "2024-02-03"],
    [4, 4, 9, "Najboljša dirkalna igra!", "2024-02-04"],
    [5, 5, 8, "Ima potencial, a potrebuje izboljšave", "2024-02-05"],
    [6, 6, 10, "Izjemna zgodba in grafika", "2024-02-06"],
    [7, 7, 7, "Dober večigralski način", "2024-02-07"],
    [8, 8, 10, "Ena najboljših iger vseh časov!", "2024-02-08"],
    [9, 9, 9, "Zabavna in inovativna", "2024-02-09"],
    [10, 10, 8, "Težka, a zelo zadovoljiva igra", "2024-02-10"]
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
