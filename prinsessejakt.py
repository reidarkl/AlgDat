__author__ = 'reidarkl'

from sys import *
import traceback
from collections import deque

def subgraftetthet(nabomatrise, startnode):
    n = len(nabomatrise)
    visited = []    # MST
    seen = deque([startnode])
    kanter = 0
    while len(seen) > 0:    # finn og sjekk hvem som er i MST fra startnode
        node = seen.popleft()
        for m in range(0, n):
            if nabomatrise[node][m] and m not in seen and m not in visited:
                seen.append(m)  # node ikke oppdaget, legg inn ny, bakerst i sett.
        visited.append(node)    # sjekket node og lagt inn de som kan ses.
    noder = n - len(visited)    # ant nodaser ikke besokt
    for k in range(0, n):   # finn kanter til noder ikke i MST.
        if k not in visited:
            for u in range(0, n):
                if nabomatrise[k][u] and u not in visited:
                    kanter += 1
    if noder == 0:
        return 0.0
    else:
        return float(kanter) / float(noder**2)


try:
    n = int(stdin.readline())
    nabomatrise = [None] * n # rader
    for i in range(0, n):
        nabomatrise[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            nabomatrise[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print("%.3f" % (subgraftetthet(nabomatrise, start) + 1E-12))
except:
    traceback.print_exc(file=stderr)
