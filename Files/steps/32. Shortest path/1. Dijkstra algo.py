def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    while heap:
        #가중치 정점
        wei, now = heapq.heappop(heap)

        #이미 처리됐으면 넘어감
        if dp[now] < wei:
            continue

        #현재 정점의 간선 순회
        for dw, du in graph[now]:
            next_wei = dw + wei
            if next_wei < dp[du]:   #최소거리를 찾으면 적용
                dp[du] = next_wei
                heapq.heappush(heap,(next_wei,du))

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