from sys import stdin
from operator import itemgetter

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    # print(nm)
    # lag hash table med plass og vekt, saa sorter etter vekt og los.
    n = len(nm)
    kanter = []
    for i in range(0, n):
        for j in range(0, n):
            if nm[i][j] is not Inf and [j, i , nm[i][j]] not in kanter: # etter and er for aa sjekke duplikat
                kanter.append([i, j, nm[i][j]]) # startnode, sluttnode, vekt
    kanter.sort(key=itemgetter(2))   # sorterer liste etter vekt.
    # print(kanter)
    tree = []
    heaviest = -1
    for m in kanter:
        if m[0] not in tree:
            tree.append(m[0])
            if m[2] > heaviest:
                heaviest = m[2]
        if m[1] not in tree:
            tree.append(m[1])
            if m[2] > heaviest:
                heaviest = m[2]
        # print(tree)
    return heaviest

linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
print(mst(nabomatrise))

