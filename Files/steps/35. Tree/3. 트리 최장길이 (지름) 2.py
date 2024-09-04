def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (n + 1)
    visited[start] = 0

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

for _ in range(n-1):
    line = list(map(int, input().split()))

    v, node, cost = line[0], line[1], line[2]

    tree[v].append((node, cost))
    tree[node].append((v, cost))

point1 = bfs(1)[0]   #1에서 제일 먼 한쪽 끝 탐색
dist = bfs(point1)[1] #한쪽 끝에서 제일 먼 다른쪽 끝 탐색

print(dist)


#트리라서 가능한 방법. 그래프면 플로이드 워셜로 max 받아야함