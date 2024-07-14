def floyd_warshall(n,graph):
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for start, end, cost in graph:
        dist[start][end] = min(dist[start][end], cost)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                dist[i][j] = 0

    return dist


import sys
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a-1, b-1, c))

result = floyd_warshall(n,edges)

for row in result:
    print(*row)