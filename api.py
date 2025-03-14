import os
from bottle import Bottle, run, template, route, request
import json
from modeli import VideoIgra, Zanr, Izdajatelj, Konzola, Ocena
import sqlite3

app = Bottle()


app.config['template_lookup'] = [os.path.join(os.path.dirname(__file__), "views")]

# Glavna stran s povezavami do kategorij
@app.route('/')
def home():
    return template('index.tpl')

# Strani za prikaz seznamov vseh kategorij
@app.route('/zanri')
def seznam_zanrov():
    zanri = Zanr.vsi_zanri()
    return template('categories.tpl', tip="žanri", elementi=zanri)

@app.route('/izdajatelji')
def seznam_izdajateljev():
    izdajatelji = Izdajatelj.vsi_izdajatelji()
    return template('categories.tpl', tip="izdajatelji", elementi=izdajatelji)

@app.route('/konzole')
def seznam_konzol():
    konzole = Konzola.vse_konzole()
    return template('categories.tpl', tip="konzole", elementi=konzole)

# Strani za prikaz iger glede na izbrano kategorijo
@app.route('/igre/zanr/<zanr>')
def igre_po_zanru(zanr):
    igre = VideoIgra.igre_po_zanru(zanr)
    return template('games.tpl', kategorija=zanr, igre=igre)

@app.route('/igre/izdajatelj/<izdajatelj>')
def igre_po_izdajatelju(izdajatelj):
    igre = VideoIgra.igre_po_izdajatelju(izdajatelj)
    return template('games.tpl', kategorija=izdajatelj, igre=igre)

@app.route('/igre/konzola/<konzola>')
def igre_po_konzoli(konzola):
    igre = VideoIgra.igre_po_konzoli(konzola)
    return template('games.tpl', kategorija=konzola, igre=igre)

# vse igre
@app.route('/igre')
def vse_igre():
    igre = VideoIgra.vse_igre()
    return template('games.tpl', kategorija="Vse igre", igre=igre)

#najbolje ocenjene igre
@app.route('/igre/najbolje-ocenejene')
def najbolje_ocenjene_igre():
    igre = VideoIgra.najbolje_ocenjene_igre()
    return template('games.tpl', kategorija="Najbolje ocenjene igre", igre=igre)


#iskanje v bazi: search bar
@app.route('/isci_igro')
def isci_igro():
    ime = request.query.get('query', '')

    conn = sqlite3.connect("igre.db")
    c = conn.cursor()

    # Poiščemo osnovne podatke o igri
    c.execute("SELECT id, ime, opis, datum_izida, starostna_omejitev FROM video_igre WHERE ime LIKE ?", (ime,))
    igra = c.fetchone()

    if igra:
        igra_id = igra[0]

        # Povprečna ocena
        c.execute("SELECT ROUND(AVG(ocena), 2) FROM ocene WHERE igra_id = ?", (igra_id,))
        povprecna_ocena = c.fetchone()[0]

        # Do 5 komentarjev
        c.execute("SELECT komentar FROM ocene WHERE igra_id = ? LIMIT 5", (igra_id,))
        komentarji = [r[0] for r in c.fetchall()]

        # Žanri
        c.execute("""
            SELECT z.naziv FROM zanri z
            JOIN igre_zanri iz ON z.id = iz.zanr_id
            WHERE iz.igra_id = ?
        """, (igra_id,))
        zanri = [r[0] for r in c.fetchall()]

        # Konzole
        c.execute("""
            SELECT k.ime FROM konzole k
            JOIN igre_konzole ik ON k.id = ik.konzola_id
            WHERE ik.igra_id = ?
        """, (igra_id,))
        konzole = [r[0] for r in c.fetchall()]

        # Izdajatelj
        c.execute("""
            SELECT i.ime FROM izdajatelji i
            JOIN igre_izdajatelj ii ON i.id = ii.izdajatelj_id
            WHERE ii.igra_id = ?
        """, (igra_id,))
        izdajatelj = c.fetchone()
        izdajatelj = izdajatelj[0] if izdajatelj else "Ni podatka"

        conn.close()

        return template('game_details.tpl',
                        igra=igra,
                        povprecna_ocena=povprecna_ocena,
                        komentarji=komentarji,
                        zanri=zanri,
                        konzole=konzole,
                        izdajatelj=izdajatelj)
    else:
        conn.close()
        return template('game_details.tpl', igra=None, iskano_ime=ime)


# Zagon strežnika
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)


