import sys
from collections import deque
sys.setrecursionlimit(150000)

def bfs(t):
    global cnt
    queue = deque([t])
    visited[t] = cnt

    while queue:
        node = queue.popleft()
        for i in sorted(line[node]):
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

##
N, M, R = map(int, sys.stdin.readline().split())
line = [ [] for _ in range(N+1) ]
visited = [0]*(N+1)
cnt = 1

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

bfs(R)

for i in range(1, N+1):
    print(visited[i])