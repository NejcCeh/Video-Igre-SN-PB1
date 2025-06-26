import sqlite3
from datetime import datetime

DATABASE = "igre.db"

def get_db_connection():
    """ustvari in vrne povezavo z bazo"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  #dostop stolpcev po imenu 
    return conn

class VideoIgra:
    @staticmethod
    def vse_igre():
        """vrne seznam vseh iger v bazi"""
        conn = get_db_connection()
        igre = conn.execute("SELECT * FROM video_igre").fetchall()
        conn.close()
        return igre

    @staticmethod
    def igre_po_zanru(zanr):
        """vrne vse igre določenega žanra"""
        conn = get_db_connection()
        igre = conn.execute("""
            SELECT video_igre.* FROM video_igre
            JOIN igre_zanri ON video_igre.id = igre_zanri.igra_id
            JOIN zanri ON igre_zanri.zanr_id = zanri.id
            WHERE zanri.naziv = ?
        """, (zanr,)).fetchall()
        conn.close()
        return igre

    @staticmethod
    def igre_po_konzoli(konzola):
        """vrne vse igre določene konzole"""
        conn = get_db_connection()
        igre = conn.execute("""
            SELECT video_igre.* FROM video_igre
            JOIN igre_konzole ON video_igre.id = igre_konzole.igra_id
            JOIN konzole ON igre_konzole.konzola_id = konzole.id
            WHERE konzole.ime = ?
        """, (konzola,)).fetchall()
        conn.close()
        return igre

    @staticmethod
    def igre_po_izdajatelju(izdajatelj):
        """vrne vse igre od določenega izdajatelja"""
        conn = get_db_connection()
        igre = conn.execute("""
            SELECT video_igre.* FROM video_igre
            JOIN igre_izdajatelj ON video_igre.id = igre_izdajatelj.igra_id
            JOIN izdajatelji ON igre_izdajatelj.izdajatelj_id = izdajatelji.id
            WHERE izdajatelji.ime = ?
        """, (izdajatelj,)).fetchall()
        conn.close()
        return igre

    @staticmethod
    def najbolje_ocenjene_igre(limit=10):
        """vrne najbolje ocenjene igre glede na povprečno oceno"""
        conn = get_db_connection()
        igre = conn.execute("""
            SELECT video_igre.*, AVG(ocene.ocena) AS povprecna_ocena
            FROM video_igre
            JOIN ocene ON video_igre.id = ocene.igra_id
            GROUP BY video_igre.id
            ORDER BY povprecna_ocena DESC
            LIMIT ?
        """, (limit,)).fetchall()
        conn.close()
        return igre
    
    @staticmethod
    def poisci_igro_po_imenu(ime):
        conn = get_db_connection()
        c = conn.cursor()

        # Iskanje po imenu (LIKE z %ime%)
        c.execute("SELECT id, ime, opis, datum_izida, starostna_omejitev FROM video_igre WHERE ime LIKE ?", ('%' + ime + '%',))
        igra = c.fetchone()

        if not igra:
            conn.close()
            return None

        igra_id = igra["id"]  # Če uporabljaš sqlite3.Row kot row_factory

        # Povprečna ocena
        c.execute("SELECT ROUND(AVG(ocena), 2) FROM ocene WHERE igra_id = ?", (igra_id,))
        povprecna_ocena = c.fetchone()[0]

        # Komentarji
        c.execute("SELECT komentar FROM ocene WHERE igra_id = ? AND komentar IS NOT NULL LIMIT 5", (igra_id,))
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

        return {
            "igra": igra,
            "povprecna_ocena": povprecna_ocena,
            "komentarji": komentarji,
            "zanri": zanri,
            "konzole": konzole,
            "izdajatelj": izdajatelj
        }

    
    @staticmethod
    def seznam_iger():
        conn = get_db_connection()
        igre = conn.execute("SELECT id, ime FROM video_igre ORDER BY id ASC").fetchall()
        conn.close()
        return igre
    
    @staticmethod
    def poisci_igro_z_detajli(ime):
        conn = get_db_connection()
        igra = conn.execute("SELECT id, ime, opis, datum_izida, starostna_omejitev FROM video_igre WHERE ime LIKE ?", (ime,)).fetchone()
        if not igra:
            conn.close()
            return None

        igra_id = igra[0]

        povprecna_ocena = conn.execute("SELECT ROUND(AVG(ocena), 2) FROM ocene WHERE igra_id = ?", (igra_id,)).fetchone()[0]

        komentarji = [r[0] for r in conn.execute("SELECT komentar FROM ocene WHERE igra_id = ? AND komentar IS NOT NULL LIMIT 5", (igra_id,))]

        zanri = [r[0] for r in conn.execute("""
            SELECT z.naziv FROM zanri z
            JOIN igre_zanri iz ON z.id = iz.zanr_id
            WHERE iz.igra_id = ?
        """, (igra_id,))]

        konzole = [r[0] for r in conn.execute("""
            SELECT k.ime FROM konzole k
            JOIN igre_konzole ik ON k.id = ik.konzola_id
            WHERE ik.igra_id = ?
        """, (igra_id,))]

        izdajatelj = conn.execute("""
            SELECT i.ime FROM izdajatelji i
            JOIN igre_izdajatelj ii ON i.id = ii.izdajatelj_id
            WHERE ii.igra_id = ?
        """, (igra_id,)).fetchone()
        izdajatelj = izdajatelj[0] if izdajatelj else "Ni podatka"

        conn.close()
        return {
            "igra": igra,
            "povprecna_ocena": povprecna_ocena,
            "komentarji": komentarji,
            "zanri": zanri,
            "konzole": konzole,
            "izdajatelj": izdajatelj
        }


class Ocena:
    @staticmethod
    def ocene_igre(id_igre):
        """vrne vse ocene in komentarje za določeno igro"""
        conn = get_db_connection()
        ocene = conn.execute("""
            SELECT ocena, komentar, datum_ocene FROM ocene
            WHERE igra_id = ?
        """, (id_igre,)).fetchall()
        conn.close()
        return ocene

    @staticmethod
    def povprecna_ocena_igre(id_igre):
        """vrne povprečno oceno za določeno igrov"""
        conn = get_db_connection()
        povprecje = conn.execute("""
            SELECT AVG(ocena) FROM ocene WHERE igra_id = ?
        """, (id_igre,)).fetchone()
        conn.close()
        return povprecje[0] if povprecje[0] is not None else None
    
    @staticmethod
    def povprecna_ocena_igre(id_igre):
        conn = get_db_connection()
        povprecje = conn.execute("SELECT AVG(ocena) FROM ocene WHERE igra_id = ?", (id_igre,)).fetchone()
        conn.close()
        return povprecje[0] if povprecje[0] else None

    @staticmethod
    def komentarji_igre(id_igre, limit=5):
        conn = get_db_connection()
        komentarji = conn.execute("""
            SELECT komentar FROM ocene
            WHERE igra_id = ? AND komentar IS NOT NULL
            LIMIT ?
        """, (id_igre, limit)).fetchall()
        conn.close()
        return komentarji

    @staticmethod
    def dodaj_oceno_komentar(igra_id, ocena, komentar):
        conn = get_db_connection()
        datum = datetime.now().strftime("%Y-%m-%d")
        conn.execute("""
            INSERT INTO ocene (igra_id, ocena, komentar, datum_ocene)
            VALUES (?, ?, ?, ?)
        """, (igra_id, ocena, komentar, datum))
        conn.commit()
        conn.close()


class Zanr:
    @staticmethod
    def vsi_zanri():
        """vrne seznam vseh žanrov"""
        conn = get_db_connection()
        zanri = conn.execute("SELECT * FROM zanri").fetchall()
        conn.close()
        return zanri

    @staticmethod
    def igre_v_zanru(zanr):
        """vrne vse igre, ki pripadajo določenemu žanru"""
        return VideoIgra.igre_po_zanru(zanr)

class Izdajatelj:
    @staticmethod
    def vsi_izdajatelji():
        """vrne seznam vseh izdajateljev"""
        conn = get_db_connection()
        izdajatelji = conn.execute("SELECT * FROM izdajatelji").fetchall()
        conn.close()
        return izdajatelji

    @staticmethod
    def igre_od_izdajatelja(izdajatelj):
        """vrne vse igre določenega izdajatelja"""
        return VideoIgra.igre_po_izdajatelju(izdajatelj)

class Konzola:
    @staticmethod
    def vse_konzole():
        """vrne seznam vseh konzol"""
        conn = get_db_connection()
        konzole = conn.execute("SELECT * FROM konzole").fetchall()
        conn.close()
        return konzole

    @staticmethod
    def igre_na_konzoli(konzola):
        """vrne vse igre, ki so na določeni konzoli"""
        return VideoIgra.igre_po_konzoli(konzola)
