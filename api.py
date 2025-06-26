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
    podatki = VideoIgra.poisci_igro_po_imenu(ime)

    if podatki:
        return template('game_details.tpl',
                        igra=podatki["igra"],
                        povprecna_ocena=podatki["povprecna_ocena"],
                        komentarji=podatki["komentarji"],
                        zanri=podatki["zanri"],
                        konzole=podatki["konzole"],
                        izdajatelj=podatki["izdajatelj"])
    else:
        return template('game_details.tpl', igra=None, iskano_ime=ime)


# Zagon strežnika
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)


