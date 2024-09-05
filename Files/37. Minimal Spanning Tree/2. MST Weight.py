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
sys.setrecursionlimit(200000)

# 입력 처리
V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))  # 가중치를 첫 번째로 두어 정렬에 유리하게 함

# 간선을 가중치 기준으로 정렬
edges.sort()

# Union-Find 자료구조 초기화
parent = [i for i in range(V + 1)]  # 1번 정점부터 V번 정점까지 사용

# Kruskal 알고리즘으로 최소 스패닝 트리 구하기
mstWeight = 0
edgeCount = 0

for edge in edges:
    weight, u, v = edge
    if find(u) != find(v):
        union(u, v)
        mstWeight += weight
        edgeCount += 1
        if edgeCount == V - 1:
            break

print(mstWeight)
