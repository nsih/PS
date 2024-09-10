def Dijkstra(start):
    dp = [INF] * (len(graph) + 1)
    dp[start] = 0
    heap = []
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

    return dp


import sys
import heapq

INF = sys.maxsize

T = int(sys.stdin.readline())

for _ in range(T):
    # 정점, 간선, 목적지 후보수
    n, m, t = map(int, sys.stdin.readline().split())
    # 출발지, g h 사이로 지나감
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        # a와 b 사이에 길이 d의 양방향 도로
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((d, b))
        graph[b].append((d, a))

        # 목적지 후보목록
        tLst = []
        for _ in range(t):
            tLst.append(int(sys.stdin.readline()))


    result = []
    for end in tLst:
        #s에서 시작해서 g->h나 h->g를 거져 tLst[i]에 도착한 거리가 최단거리인가?
        dp = Dijkstra(s)

        dp1 = Dijkstra(g)
        dp2 = Dijkstra(h)

        if dp[end] == dp[g] + dp1[h] + dp2[end] or dp[end] == dp[h] + dp2[g] + dp1[end]:
            result.append(end)

    result.sort()
    print(*result)