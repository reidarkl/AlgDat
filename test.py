__author__ = 'reidarkl'

from collections import deque
from sys import *

stack = [1, 2, 3, 4, 5]

for i in stack:
    print(i)

print(stack[len(stack) - 1])
print(stack.pop())

a = [1, 2, 3]
depth = 123
que = [(a, depth), ('hei', 'skjer')]
# print(a.pop())
print(que.pop())
print(que.pop())

b = [1, 2]

qu = deque((b, depth))
que = deque(b)
print(que.popleft())
print(qu.popleft())

b = ["hei", "på", "bok"]
for i in b:
    for j in i:
        print(j)

if "hei" in b:
    print("jepp")

c = 3
print(c/2)

alist = [(1, 2), (1, 4)]
print(alist[1][1])

aalist = [[(1,'i'),(3,'i'),(5,'i'),(8,'i')], [(2,'n')], [(4,'t'),(7,'t')], [(6,'a')], [(9,'v')]]
print(aalist[0][0])

asd = [1, 2, 3, 4]
asb = [3, 4, 5, 6]

for i in asd:
    print(i)
for i in asb:
    print(i)
