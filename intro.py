__author__ = 'reidarkl'

from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    maks = 0
    while kubbe is not None:
        if kubbe.vekt > maks:
            maks = kubbe.vekt
        kubbe = kubbe.neste
    return maks

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste is None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print(spor(forste))
