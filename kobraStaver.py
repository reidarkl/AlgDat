__author__ = 'reidarkl'



from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    topnode = Node() #starter noder
    for (o, pos) in ordliste: #ga gjennom ordliste, ma sa ta bokstav for bokstav.
        node = topnode #for hvert ord, start i toppnode
        for b in o:
            if b not in node.barn:
                node.barn[b] = Node() #hvis bokstav ikke er i barna, ma det lages ny node for det.
            node = node.barn[b] #hekter seg pa nedover treet om bokstaven er i treet/lagt til.
        node.posi.append(pos) #legg inn posisjon nar ord er ferdig.
    return topnode


def posisjoner(ord, indeks, node):
    if indeks >= len(ord):
        pos = node.posi
    elif ord[indeks] == '?':
        pos = []
        for b in node.barn:
            pos += posisjoner(ord, indeks+1, node.barn[b])
    elif ord[indeks] in node.barn: #sjekker bokstaven er i ordet
        pos = posisjoner(ord, indeks+1, node.barn[ord[indeks]])
    else:
        pos = []
    # print(pos)
    return pos
    # SKRIV DIN KODE HER


try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)