# Video-Igre-SN-PB1
Seminarska naloga pri predmetu podatkovne baze 1
Imeli bomo glavno tabelo video_igre. V tej imamo dostop do podatkov: id, ime, tekstovni
opis, starostno omejitev, datum izida.
Nato bomo imeli tabelo izdajatelj, kjer bodo podatki: id, ime, država, leto, spletna stran. 
Za vsako igro je lahko več izdajateljev, torej imamo povezavo 1:n
Podobno je pri tabeli ocene, ki bodo vsebovale: id, ocena, komentar in datum ocene. 
Nato pa imamo še tabeli konzole in žanr, ki pa se povezujeta z glavno tablo iger n:n, saj
ima lahko več iger več žanrov in konozol. Konzole bodo vsebovale: id ime, datum izida,
proizvajalec, generacija.
Tabela žanr bo imela id in naziv.
