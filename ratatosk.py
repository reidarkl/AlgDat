__author__ = 'reidarkl'
from sys import stdin
from collections import deque


class Node:
    barn = None
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS

    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    stack = [rot]
    while len(stack) is not 0:
        node = stack[len(stack) - 1]  # posisjonen til siste lagt inn
        if node.ratatosk:
            return len(stack) - 1  # samme logikk som over
        if node.nesteBarn == len(node.barn):  # alle barn besokt
            stack.pop()
        else:
            stack.append(node.barn[node.nesteBarn])
            node.nesteBarn += 1
    # SKRIV DIN KODE HER

def bfs(rot):
    depth = 0
    que = [(rot, depth)]  # mulig aa bruke dequeu? faar ikke til.
    while len(que) != 0:
        node, depth = que.pop(0)
        if node.ratatosk:
            return depth
        for j in node.barn:
            que.append((j, depth+1))

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print(dfs(start_node))
elif funksjon == 'bfs':
    print(bfs(start_node))
elif funksjon == 'velg':
    dfs(start_node)

