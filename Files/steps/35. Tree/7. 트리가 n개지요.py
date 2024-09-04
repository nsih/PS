def countTree(n, tree):
    visited = [False] * (n + 1)
    treeCount = 0

    # DFS
    def isTree(v, parent):
        visited[v] = True
        for node in tree[v]:
            if not visited[node]:
                if not isTree(node, v):
                    return False
            elif node != parent:
                # 방문한 적이 있는데 부모가 아니면 사이클이 존재하니까 그래프 (트리x)
                return False
        return True

    for i in range(1, n + 1):
        if not visited[i]:  #방문한적없으면 트리확인
            if isTree(i, -1):
                treeCount += 1
    return treeCount


import sys
sys.setrecursionlimit(200000)

case = 0
while True:
    case += 1
    n,m = map(int,sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    temp = [[] for _ in range(n + 1)]

    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())

        temp[a].append(b)
        temp[b].append(a)

    count = count_trees(n,temp)


    print(f'Case {case}: ', end='')

    if count == 0:
        print('No trees.')
    elif count == 1:
        print('There is one tree.')
    else:
        print(f"A forest of {count} trees.")