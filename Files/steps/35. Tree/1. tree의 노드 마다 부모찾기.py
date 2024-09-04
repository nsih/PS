def bfs(root):
    queue = deque([root])
    parent[root] = -1  # 루트의 부모는 없으므로 -1로 설정

    while queue:
        current = queue.popleft()

        for neighbor in tree[current]:
            if parent[neighbor] == 0:
                parent[neighbor] = current
                queue.append(neighbor)



from collections import deque
import sys

n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [0] * (n + 1)

bfs(1)

for i in range(2, len(parent)):
    print(parent[i])
