#섬 대 섬으로 간선연결 되는지 확인하고, 특정 섬으로 향하는 여러 간선중 최소비용인 간선만 저장
#확인한 간선보고 MST로 압축 못하면 -1출력
#되면 구해놓은 간선들로 mst 간선 길이 출력




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

n,m = map(int, sys.stdin.readline().split())

#vertex cord
vertexs = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    vertexs.append((x, y))

#edge
edges = []
originalEdge = set()
for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())

    v1 -= 1
    v2 -= 1

    x1, y1 = vertexs[v1]
    x2, y2 = vertexs[v2]

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    edges.append((dist, v1, v2))
    originalEdge.add((min(v1, v2), max(v1, v2)))

#추가할 간선
additionalEdges = []
for i in range(n):
    for j in range(i + 1, n):
        if (min(i, j), max(i, j)) not in originalEdge:
            x1, y1 = vertexs[i]
            x2, y2 = vertexs[j]
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            additionalEdges.append((dist, i, j))

edges.sort()
additionalEdges.sort()

#MST
parent = [i for i in range(n)]

# Kruskal
mstWeight = 0
edgeCount = 0

#original edge
for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mstWeight += weight
        edgeCount += 1

#additional adge
additionalWeight = 0
for weight, u, v in additionalEdges:
    if find(u) != find(v):
        union(u, v)
        mstWeight += weight
        additionalWeight += weight
        edgeCount += 1
        if edgeCount == n - 1:  # 모든 정점이 연결되면 종료
            break

print(f"{additionalWeight:.2f}")