import sys

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [input().rstrip() for _ in range(N)]

sumLst = [[0]*(M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            if lst[i-1][j-1] == 'B':
                sumLst[i][j] = sumLst[i - 1][j] + sum[i][j - 1] + sum[i - 1][j - 1]
            else:
                sumLst[i][j] = sumLst[i - 1][j] + sum[i][j - 1] + sum[i - 1][j - 1] + 1
        else:
            if lst[i-1][j-1] == 'W':
                sumLst[i][j] = sumLst[i-1][j] + sumLst[i][j-1] + sumLst[i-1][j-1]
            else:
                sumLst[i][j] = sumLst[i - 1][j] + sumLst[i][j - 1] + sumLst[i - 1][j - 1] +1


max_ = 0
min_ = 0
for i in range(K, N+1):
    for j in range(K, M+1):
        max_ = max(sumLst[i][j] - sum)


print(ans)