def bellman_ford(start):
    #start 도시에서 출발
    dist[start] = 0

    # n번의 라운드를 반복
    for i in range(1, n + 1):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == n:
                    return True

    return False


import sys
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우
        if dist[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(dist[i])