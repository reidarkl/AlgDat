__author__ = 'reidarkl'

from sys import stdin

def binsok(alist, val):
    imin = 0
    imax = len(alist) - 1
    while imin <= imax:
        imid = (imin + imax) // 2
        if alist[imid] == val:
            break
        elif alist[imid] < val:
            imin = imid + 1
        else:
            imax = imid - 1
    return imid


def sorter(a):
    # Merk: den sorterte lista ma returneres
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        sorter(left)
        sorter(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a



def finn(A, nedre, ovre):
    # Merk: resultatet ma returneres
    lowIndex = binsok(A, nedre)
    highIndex = binsok(A, ovre)
    if A[lowIndex] > nedre and lowIndex != 0:
        lowIndex -= 1
    if A[highIndex] < ovre and highIndex != len(A)-1:
        highIndex += 1
    return [A[lowIndex], A[highIndex]]

liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)

for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])

