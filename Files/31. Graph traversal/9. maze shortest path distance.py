def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = deque([(0,0,1)])
    visitedBFS[0][0] = True

    while Q:
        x, y, dist = Q.popleft()

        for dx,dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '1' and not visitedBFS[nx][ny]:
                    if nx == N-1 and ny == M-1:
                        return dist
                    Q.append((nx, ny, dist+1))
                    visitedBFS[nx][ny] = True

####
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

matrix = []

for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

bfsCnt = []
visitedBFS = [[False]*M for _ in range(N)]

print(bfs()+1)