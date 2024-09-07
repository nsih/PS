def bfs(start,end):
    x,y = start
    cnt = 0
    Q = deque([(x,y,cnt)])

    while Q:
        horseDir = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        x,y,cnt = Q.popleft()

        for dx,dy in horseDir:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix) and not matrix[nx][ny]:
                if nx == end[0] and ny == end[1]:
                    return cnt+1
                Q.append((nx,ny, cnt + 1))
                matrix[nx][ny] = True

from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())

    sx,sy = map(int,sys.stdin.readline().split())
    ex,ey = map(int, sys.stdin.readline().split())

    matrix = [[False]*I for _ in range(I)]

    if (sx, sy) == (ex, ey):
        print(0)
    else:
        print(bfs((sx, sy), (ex, ey)))