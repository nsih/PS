def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    while heap:
        #가중치, 정점
        wei, now = heapq.heappop(heap)

        #더 짧은게 있으면 그냥 놔둠
        if dp[now] < wei:
            continue

        #현재 정점의 간선 순회
        for dw, du in graph[now]:
            nextWei = dw + wei
            if nextWei < dp[du]:   #최소거리를 찾으면 적용
                dp[du] = nextWei
                heapq.heappush(heap,(nextWei,du))

import sys
import heapq

INF = sys.maxsize
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])