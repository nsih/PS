def bfs(start):
    dice = [1,2,3,4,5,6]
    Q = deque([(start,1)])

    while Q:
        x,cnt = Q.popleft()

        for dx in dice:
            nx = x+dx

            if nx == 100:
                return cnt

            if 0 <= nx < 101:
                if not visited[nx]:
                    visited[nx] = True

                    if graph[nx]:
                        visited[nx] = True
                        nx = graph[nx]
                        Q.append((nx, cnt + 1))
                    else:
                        Q.append((nx, cnt + 1))


from collections import deque
import sys

N,M = map(int, sys.stdin.readline().split())

graph = [0] * 101
visited = [False] * 101

for _ in range(N+M):
    v,u = map(int, sys.stdin.readline().split())
    graph[v] = u

print(bfs(1))