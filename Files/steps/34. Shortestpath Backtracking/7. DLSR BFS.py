import sys
from collections import deque

def BFS(A, B):
    max_limit = 10000

    visitedLst = [False] * max_limit
    prevLst = [None] * max_limit

    visitedLst[A] = True
    Q = deque([A])

    while Q:
        n = Q.popleft()

        for next_n, nextC in ((n * 2 % 10000, 'D'),
                              (n - 1 if n != 0 else 9999, 'S'),
                              (((n % 1000) * 10 + n // 1000) % 10000, 'L'),
                              (((n % 10) * 1000 + n // 10) % 10000, 'R')):

            if not visitedLst[next_n]:  #방문 안했으면
                visitedLst[next_n] = True
                prevLst[next_n] = (n, nextC)

                if next_n == B:
                    return prevLst

                Q.append(next_n)

    return prevLst

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    result = BFS(A, B)
    path = []
    idx = B

    while idx != A:
        path.append(result[idx][1])
        idx = result[idx][0]

    print(''.join(reversed(path)))