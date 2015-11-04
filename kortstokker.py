from sys import stdin
from itertools import repeat

# [[(1,'i'),(3,'i'),(5,'i'),(8,'i')], [(2,'n')], [(4,'t'),(7,'t')], [(6,'a')], [(9,'v')]]

def merge(decks):
    if len(decks) > 1:
        mid = len(decks) // 2
        left = decks[:mid]
        right = decks[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                decks[k] = left[i]
                i += 1
            else:
                decks[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            decks[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            decks[k] = right[j]
            j += 1
            k += 1
    text = []
    for m in range(0, len(decks)):
        text.append(decks[m][1])
        # print(text)
    return "".join(text)

def makeDecks(decks):
    newDecks = []
    # newDecks.append(decks[0][0])
    # newDecks.append(decks[1][0])
    for i in range(0, len(decks)):
        for j in range(0, len(decks[i])):
            newDecks.append(decks[i][j])
    return newDecks


decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
decks = makeDecks(decks)
print merge(decks)
