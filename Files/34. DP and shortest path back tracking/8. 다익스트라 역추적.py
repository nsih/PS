def Dijkstra(start):
    dp = [INF] * (len(graph) + 1)
    dp[start] = 0

    #이전 도시 저장
    prePos = [-1] * (len(graph) + 1)

    #
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
                prePos[du] = now

    return dp,prePos


import sys
import heapq

INF = sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    # 정점, 간선, 코스트
    a, b, d = map(int, sys.stdin.readline().split())
    graph[a].append((d, b)) #코스트 간선

start, end = map(int, sys.stdin.readline().split())

cost,prePos = Dijkstra(start)

#최소비용
print(cost[end])

#거치는 도시 수, 거치는 도시
path = []
current = end
while current != -1:
    path.append(current)
    current = prePos[current]
path.reverse()

print(len(path))
print(*path)