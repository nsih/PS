def dfs(t):
    visitedDFS[t] = True
    dfs_order.append(t)
    for i in graph[t]:
        if not visitedDFS[i]:
            dfs(i)

def bfs(t):
    Q = deque([t])
    visitedBFS[t] = True
    bfs_order.append(t)

    while Q:
        c = Q.popleft()
        for i in graph[c]:
            if not visitedBFS[i]:
                visitedBFS[i] = True
                bfs_order.append(i)
                Q.append(i)

####
import sys
from collections import deque
sys.setrecursionlimit(150000)

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1, N + 1):
    graph[node].sort()

visitedDFS = [False] * (N + 1)
dfs_order = []
dfs(V)
print(*dfs_order)


visitedBFS = [False] * (N + 1)
bfs_order = []
bfs(V)
print(*bfs_order)