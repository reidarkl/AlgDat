__author__ = 'reidarkl'

from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
    # expand nodes, and add source - drain.
    n = len(kapasiteter)
    exp_n = 2*n+2  # number of nodes in expanded. Split existing, add s, d
    matrix = []
    for i in range(exp_n):
        matrix.append([0]*exp_n)  # new matrix with 0's.
    for i in startrom:  # connect nodes to super source
        matrix[0][i*2+1] = 1
    for i in utganger:  # connect nodes to drain
        matrix[2*i+2][exp_n-1] = 1
    for i in range(n):  # put in existing float
        for j in range(n):
            matrix[2*i+2][2*j+1] = kapasiteter[i][j]
    for i in range(n):
        matrix[2*i+1][2*i+2] = 1  # set capacity between splitted nodes
    # new matrix with source and drain complete.
    m = len(matrix)
    floats = []
    source = 0
    drain = m-1
    paths = 0
    # print(matrix)
    for i in range(m):
        floats.append([0] * m)

    while True:
        path = finnFlytsti(source, drain, floats, matrix)
        if not path:
            return paths
        for i in range(len(path)-1):
            floats[path[i]][path[i+1]] += 1
            floats[path[i+1]][path[i]] -= 1
        paths += 1
        if paths == len(startrom):
            return paths
# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene,
# siste element er indeksen til en av utgangene, og elementene imellom er
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

noder, _, _ = [int(x) for x in stdin.readline().split()]
startrom = [int(x) for x in stdin.readline().split()]
utganger = [int(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    nabomatrise.append(naborad)
print(antallIsolerteStier(nabomatrise, startrom, utganger))
