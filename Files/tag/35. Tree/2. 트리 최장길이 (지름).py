def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (n + 1)
    visited[start] = 0.

    result = [0, 0]

    while q:
        node, cost = q.popleft()

        for nextNode, nextCost in tree[node]:
            if visited[nextNode] == -1:
                calcCost = cost + nextCost
                q.append((nextNode, calcCost))
                visited[nextNode] = calcCost
                if result[1] < calcCost:
                    result[0] = nextNode
                    result[1] = calcCost

    return result


from collections import deque
import sys
INF = int(1e9)

n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]

for _ in range(n):
    line = list(map(int, input().split()))
    v = line[0]
    idx = 1
    while line[idx] != -1:
        node, cost = line[idx], line[idx+1]
        tree[v].append((node, cost))
        idx += 2

point1 = bfs(1)[0]   #1에서 제일 먼 한쪽 끝 탐색
point2 = bfs(point1)[1] #한쪽 끝에서 다른쪽 끝 탐색
print(point2)


#트리라서 가능한 방법. 그래프면 플로이드 워셜로 max 받아야함