import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  lst.append([a, b])
lst.sort()

dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i],dp[j]+1)


print(n-max(dp))
