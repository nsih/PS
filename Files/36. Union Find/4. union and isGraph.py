def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB



import sys
sys.setrecursionlimit(200000)

n, m = map(int,sys.stdin.readline().split())

parent = [i for i in range(n)]

cnt = 1
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())

    if find(a) == find(b):
        print(cnt)
        break

    union(a,b)
    cnt += 1

else:
    print(0)