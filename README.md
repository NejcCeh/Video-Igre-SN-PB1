Projekt, ki ga ustvarjava Nejc Čeh in Alen Rajšel, v okviru predmeta Podatkovne Baze 1, je namenjen brskanju po bazi video iger. Ustvarila sva bazo podatkov v SQLite, ki ima podatke o video igrah. 
Na voljo je 200 različnih igrah, med katerimi lahko iščemo različne žanre, izdajatelje, dobimo podatke kot so: leto izdaje, konzole, na katerih je mogoče igro igrati, opis igre, starostna omejitev in tako dalje.
V kolikor najdemo kakšno igro, ki nam je všeč, si lahko ogledamo igre z enakim žanrom, ali tiste istega proizvajalca/izdajatelja. 
Ogledamo si lahko tudi ocene za te igre, ter dodamo tudi svojo oceno in komentar. 

Projekt je razdeljen na več datotek:
Data.py s spetne strani https://rawg.io/ pobere podatke o 200 video igrah in jih primerno uredi, v csv datoteke. 
Setup_baza.py ustvari ustrezne tabele za bazo v SQLite.
import_csv.py v bazo uvozi vse podatke pridobljene s spletne strani.
modeli.py predstavlja modele sql poizvedb za pridobivanje ustreznih podatkov iz baze.
api.py spletni vmesnik.
cli.py tekstovni vmesnik.
