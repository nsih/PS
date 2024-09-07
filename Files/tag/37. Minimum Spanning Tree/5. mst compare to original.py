def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

import sys
import math
sys.setrecursionlimit(200000)

#집, 길
while True:
    m,n = map(int, sys.stdin.readline().split())

    if m == 0 and n == 0:
        break

    #vertex cord
    vertexs = [i for i in range(m)]

    edges = []
    originalWeight = 0
    for _ in range(n):
        x, y, weight = map(int, sys.stdin.readline().split())
        edges.append((weight, x, y))
        originalWeight += weight

    edges.sort()

    #MST
    parent = [i for i in range(m)]

    # Kruskal
    mstWeight = 0
    edgeCount = 0

    #original edge
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mstWeight += weight
            edgeCount += 1

    print(originalWeight-mstWeight)