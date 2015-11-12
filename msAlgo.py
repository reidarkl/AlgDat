from sys import stdin, maxint


def korteste_rute(rekkefolge, nabomatrise, byer):
    matrise = floydbrur(nabomatrise, byer)
    path = 0
    for by in range(len(rekkefolge)):
        """if by == len(rekkefolge) - 1:
            path += matrise[rekkefolge[0]][rekkefolge[len(rekkefolge) - 1]]
            break"""
        path += matrise[rekkefolge[by]][rekkefolge[(by + 1) % byer]]
    if path >= maxint / 3:
        path = 'umulig'
    return path

def floydbrur(nabomatrise, byer):  # s 695
    for k in range(byer):
        for i in range(byer):
            for j in range(byer):
                nabomatrise[i][j] = min(nabomatrise[i][j], nabomatrise[i][k] + nabomatrise[k][j])
    return nabomatrise

testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = [int(by) for by in stdin.readline().split()]  # rekkefolgen de maa besokes
    nabomatrise = []  # tom matrise.
    for by in range(byer):
        row = []
        for road in stdin.readline().split():
            dist = int(road)
            if dist == -1:
                dist = maxint / 3
            row.append(dist)
        nabomatrise.append(row)
    print korteste_rute(rekkefolge, nabomatrise, byer)


