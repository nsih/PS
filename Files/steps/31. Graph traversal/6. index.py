def bfs(t):
    cntBFS = 1
    Q = deque([t])
    visitedBFS[t] = cntBFS

    while Q:
        c = Q.popleft()
        for i in graph[c]:
            if visitedBFS[i] == 0:
                cntBFS += 1
                visitedBFS[i] = cntBFS
                Q.append(i)

def dfs(t):
    global cntDFS
    visitedDFS[t] = cntDFS
    graph[t].sort()

    for i in graph[t]:
        if visitedDFS[i] == 0:
            cntDFS += 1
            visitedDFS[i] = cntDFS
            dfs(i)

###
import sys
from collections import deque
sys.setrecursionlimit(150000)

N,M,V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1, N + 1):
    graph[node].sort()

cntDFS = 1
visitedDFS = [0]*(N+1)
dfs(V)
print(*visitedDFS[1:])

visitedBFS = [0]*(N + 1)
bfs(V)
print(*visitedBFS[1:])