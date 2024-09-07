def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return

    parent[rootA] = rootB
    count[rootB] += count[rootA]
    return


import sys
sys.setrecursionlimit(200000)

T = int(sys.stdin.readline())

for _ in range(T):
    F = int(sys.stdin.readline())

    parent = dict()
    count = dict()

    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())

        if a not in parent:
            parent[a] = a
            count[a] = 1

        if b not in parent:
            parent[b] = b
            count[b] = 1

        union(a, b)

        print(count[find(a)])