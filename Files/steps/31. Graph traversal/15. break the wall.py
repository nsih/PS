def bfs(start):
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    x,y = start

    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    breakVisited = [[False] * M for _ in range(N)]

    Q = deque([(x,y,1,False)])

    while Q:
        x, y, cnt, flag = Q.popleft()

        for dx,dy in dir:
            nx = x + dx
            ny = y + dy

            if nx == M-1 and ny == N-1:
                return cnt+1

            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] == '1':   #벽이면
                    if not flag and not breakVisited[ny][nx]: #벽 안부순 상태면
                        breakVisited[ny][nx] = True
                        Q.append((nx,ny,cnt+1,True))

                else:   #벽아니면
                    if not flag and not visited[ny][nx]:    #벽 안부순 상태면
                        visited[ny][nx] = True
                        Q.append((nx, ny, cnt + 1, flag))

                    elif flag and not breakVisited[ny][nx]: #벽 부순 상태면
                        breakVisited[ny][nx] = True
                        Q.append((nx, ny, cnt + 1, flag))
    return -1

from collections import deque
import sys

N,M = map(int, sys.stdin.readline().split())
matrix = [sys.stdin.readline().strip() for _ in range(N)]

if N == 1 and M == 1:
    print(1)
else:
    print(bfs((0,0)))