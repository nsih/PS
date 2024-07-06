def bfs(N, K):
    max_limit = 100001

    visitedLst = [False] * max_limit
    visitedLst[N] = True

    Q = deque([(N, 0)])

    while Q:
        n, steps = Q.popleft()

        for next_n in (n * 2, n + 1, n - 1):
            if 0 <= next_n < max_limit and not visitedLst[next_n]:
                if next_n == K:
                    return steps + 1
                Q.append((next_n, steps + 1))
                visitedLst[next_n] = True

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

if N == K:
    print(0)
else:
    print(bfs(N, K))