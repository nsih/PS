#그래프 탐색으로 행렬의 섬 구분
#섬 대 섬으로 간선연결 되는지 확인하고, 특정 섬으로 향하는 여러 간선중 최소비용인 간선만 저장
#확인한 간선보고 MST로 압축 못하면 -1출력
#되면 구해놓은 간선들로 mst 간선 길이 출력


def bfs(x, y, islandNumber):
    queue = deque([(x, y)])
    matrix[x][y] = islandNumber

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우 네 방향 탐색
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = islandNumber
                queue.append((nx, ny))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

from collections import deque
import sys
sys.setrecursionlimit(200000)


n,m = map(int, sys.stdin.readline().split())

matrix = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    matrix.append(lst)

#island partition ( BFS로 1이면 islandNumber 붙임 )
islandNumber = 2

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            bfs(i, j, islandNumber)
            islandNumber += 1

islandCnt = islandNumber - 2

#edge 추가
edge = []
minEdge = {}    # key u,v  value distance

for i in range(n):
    for j in range(m):
        if matrix[i][j] >= 2:  # 섬이라면
            currentIsland = matrix[i][j]

            # 상하좌우 네 방향에 대해 섬을 뻗어나가기
            for d in range(4):
                nx, ny = i, j
                dist = 0

                while True:
                    nx += dx[d]
                    ny += dy[d]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위
                        break
                    if matrix[nx][ny] == currentIsland:  # 같은 섬을 만나면 중단
                        break
                    if matrix[nx][ny] == 0:  # 0이면 진행, 거리+
                        dist += 1
                    elif matrix[nx][ny] >= 2:  # 다른 섬 찾음
                        if dist > 1:  # 거리가 2 이상인 경우만 간선으로 처리
                            otherIsland = matrix[nx][ny]
                            # 최소거나 최초일때 추가
                            if (currentIsland, otherIsland) not in minEdge or minEdge[(currentIsland, otherIsland)] > dist:
                                minEdge[(currentIsland, otherIsland)] = dist
                                minEdge[(otherIsland, currentIsland)] = dist  # 간선 추가
                        break

# 중복 제거후 정렬
edge = [(dist, u, v) for (u, v), dist in minEdge.items()]
edge.sort()

#mst
parent = [i for i in range(islandCnt + 2)]
mstWeight = 0
edgeCount = 0

for weight, u, v in edge:
    if find(u) != find(v):
        union(u, v)
        mstWeight += weight
        edgeCount += 1
        if edgeCount == islandCnt - 1:
            break

#mst트리가 성립하면 mstWeight출력, 아니면 -1 출력
if edgeCount == islandCnt - 1:
    print(mstWeight)
else:
    print(-1)