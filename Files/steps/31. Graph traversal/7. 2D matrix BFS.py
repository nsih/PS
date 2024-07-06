def bfs(start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = deque([start])
    visitedBFS[start[0]][start[1]] = True
    cnt = 1

    while Q:
        x, y = Q.popleft()

        for dx,dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == '1' and not visitedBFS[nx][ny]:
                    Q.append((nx,ny))
                    visitedBFS[nx][ny] = True
                    cnt += 1
    bfsCnt.append(cnt)

####
import sys
from collections import deque

N = int(sys.stdin.readline())

matrix = []

for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

bfsCnt = []
visitedBFS = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and not visitedBFS[i][j]:
            bfs((i,j))

print(len(bfsCnt))
bfsCnt.sort()
for i in bfsCnt:
    print(i)