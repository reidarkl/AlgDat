__author__ = 'reidarkl'

from sys import stdin

def minCoinsGreedy(coins, value):
    # SKRIV DIN KODE HER

def minCoinsDynamic(coins, value):
    # SKRIV DIN KODE HER

def canUseGreedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER

Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print minCoinsGreedy(coins, int(line))
else:
    for line in stdin:
        print minCoinsDynamic(coins, int(line))