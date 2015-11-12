__author__ = 'reidarkl'

from sys import stdin, maxint


def minCoinsGreedy(coins, value):
    tempV = 0
    coin = 0
    for c in coins:
        while c + tempV <= value:
            tempV += c
            coin += 1
    return coin

def minCoinsDynamic(coins, value):
    if value in coins:
        return 1
    c = [0]
    for i in range(1, value + 1):
        q = maxint  # q = min_coins
        for j in range(0, len(coins)):
            if coins[j] <= i:  # sjekker at coin ikke er for stor.
                if 1 + c[i - coins[j]] < q:  # c[i - coins[j]] skaffer ant. coins i hoyeste posisjon nar nye storste er inne.
                    q = 1 + c[i - coins[j]]
        c.append(q)
    return c.pop()



def canUseGreedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    pass

Inf = 1000000000
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()  # stor -> lav sortering
print coins
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
    for line in stdin:
        print minCoinsGreedy(coins, int(line))
else:
    for line in stdin:
        print minCoinsDynamic(coins, int(line))
