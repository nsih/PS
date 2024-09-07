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

# 별들의 좌표 입력 받기
n = int(sys.stdin.readline())  # 별의 개수


#vertex
vertexs = []
for _ in range(n):
    x, y = map(float, input().split())
    vertexs.append((x, y))

#edge
edges = []
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = vertexs[i]
        x2, y2 = vertexs[j]

        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        edges.append((dist, i, j))
edges.sort()


#MST
parent = [i for i in range(n)]

# Kruskal
mstWeight = 0
edgeCount = 0

for edge in edges:
    weight, u, v = edge
    if find(u) != find(v):
        union(u, v)
        mstWeight += weight
        edgeCount += 1
        if edgeCount == n - 1:
            break

print(mstWeight)