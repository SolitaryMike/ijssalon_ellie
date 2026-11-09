from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)

    nieuwe_prijs_tekst = f"{nieuwe_prijs:.2f}".replace(".", ",")

    tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs_tekst} euro."

    return tekst


def inkomsten_totaal(inkomsten, btw):
    totaal = 0

    for bedrag in inkomsten:
        totaal += bedrag

    btw_bedrag = totaal * btw

    tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

    return tekst

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)

    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)

    gemiddeld_bedrag = totaal / aantal

    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)

    resultaat = mijn_functie_2(korte_lijst[0], korte_lijst[1])

    return resultaat