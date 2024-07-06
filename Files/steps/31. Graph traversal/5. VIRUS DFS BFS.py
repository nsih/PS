def bfs():
    Q = deque([1])  #1에서 시작

    while Q:
        c = Q.popleft()
        for i in graph[c]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = 1

def dfs(t):
    visited[t] = 1
    graph[1].sort()
    for i in graph[t]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

import sys
from collections import deque
sys.setrecursionlimit(150000)

###
N = int(sys.stdin.readline())   #정점
M = int(sys.stdin.readline())   #간선

graph = [[] for _ in range(N+1)]
graph.sort()

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [0]*(N+1)
visited[1] = 1

dfs(1)

print(sum(visited)-1)