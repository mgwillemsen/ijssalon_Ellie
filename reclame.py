from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
    return tekst

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag

    btw_bedrag = totaal * btw

    tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    return tekst
week = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gem= totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gem:.2f} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])
