import sys

n,k = map(int,sys.stdin.readline().split())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,k+1):
        if lst[i - 1][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(lst[i-1][1] + dp[i-1][j-lst[i-1][0]],dp[i-1][j])

print(dp[-1][-1])