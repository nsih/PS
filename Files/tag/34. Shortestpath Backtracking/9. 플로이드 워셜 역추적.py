def floyd_warshall(n,graph):
    dist = [[INF] * n for _ in range(n)]

    path = [[-1] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for start, end, cost in graph:
        dist[start][end] = min(dist[start][end], cost)
        path[start][end] = start  #초기 경로는 연결된 정점으로 설정

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]  # k를 거쳐가는 경로로 업데이트

    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                dist[i][j] = 0

    return dist,path


def PathTracking(path, start, end):
    if path[start][end] == -1:
        return []  # 경로가 없으면 빈 리스트 반환

    route = []
    current = end

    # 경로 추적
    while current != start:
        route.append(current + 1)  # idx
        current = path[start][current]

    route.append(start + 1)
    route.reverse()

    return route



import sys

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a-1, b-1, c))

distances, path = floyd_warshall(n,edges)

for row in distances:
    print(*row)


#없으면 0, 있으면 길이, 경로
for i in range(n):
    for j in range(n):
        if i == j or distances[i][j] == 0:
            print(0)
        else:
            path_route = PathTracking(path, i, j)
            if path_route:
                print(len(path_route), ' '.join(map(str, path_route)))
            else:
                print(0)