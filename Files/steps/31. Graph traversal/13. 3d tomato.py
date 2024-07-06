def bfs(start,M,N,H):
    dir = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
    Q = deque(start)

    while Q:
        x,y,h,day = Q.popleft()
        for dx,dy,dh in dir:
            nx = x+dx
            ny = y+dy
            nh = h+dh

            if 0 <= nx < M and 0 <= ny < N and 0 <= nh < H:   #범위 내
                if lst[nh][ny][nx] == 0:    #익지 않은 토마토가 주변에 있으면
                    lst[nh][ny][nx] = 1
                    Q.append((nx,ny,nh,day+1))

    return day

from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
lst = []

for _ in range(H):
    floor = []
    for _ in range(N):
        floor.append(list(map(int, sys.stdin.readline().split())))
    lst.append(floor)

starts = []
for k in range(H):
    for i in range(N):
        for j in range(M):
            if lst[k][i][j] == 1:
                starts.append((j, i, k, 0))

if not starts:
    print(-1)
else:
    days = bfs(starts, M, N, H)

    if any(0 in row for floor in lst for row in floor):
        print(-1)
    else:
        print(days)