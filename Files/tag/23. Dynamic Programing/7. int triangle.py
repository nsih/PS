import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

dp = [[0]*n for _ in range(n)]

arr = [list(map(int,sys.stdin.readline().split()))for _ in range(n)]


dp[0][0] = arr[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n-1]))