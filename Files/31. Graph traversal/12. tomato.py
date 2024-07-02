def bfs(start,M,N):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    Q = deque(start)

    while Q:
        x,y,day = Q.popleft()
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < M and 0 <= ny < N:   #범위 내
                if lst[ny][nx] == 0:    #익지 않은 토마토가 주변에 있으면
                    lst[ny][nx] = 1
                    Q.append((nx,ny,day+1))

    return day

from collections import deque
import sys

M,N = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

starts = []
day = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            starts.append((j,i,0))

if not starts:
    print(-1)
else:
    days = bfs(starts, M, N)

    if any(0 in sublist for sublist in lst):
        print(-1)
    else:
        print(days)