def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


import sys
sys.setrecursionlimit(200000)

#n, m = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n)]

#n번째 노드의 연결상태 갱신
for i in range(n):
    connect = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if connect[j] == 1:
            union(i, j)

rLst = list(map(int, sys.stdin.readline().split()))

# rLst의 첫 번째 원소를 기준으로 설정
root = find(rLst[0] - 1)  # 인덱스 0부터 시작하는 배열을 고려하여 -1

# rLst의 모든 원소가 같은 루트를 가리키는지 확인
result = all(find(rLst[i] - 1) == root for i in range(1, len(rLst)))

if result:
    print("YES")
else:
    print("NO")