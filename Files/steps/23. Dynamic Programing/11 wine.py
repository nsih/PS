import sys

n = int(sys.stdin.readline())

lst = [0]*10001
dp = [0]*10001

for i in range(1,n+1):
    lst[i] = int(sys.stdin.readline())

dp[1] = lst[1]
dp[2] = lst[1]+lst[2]
dp[3] = max(lst[1]+lst[3], lst[2]+lst[3],dp[2])

for i in range(4,n+1):
    dp[i] = max(lst[i] + lst[i-1] + dp[i-3], lst[i] + dp[i-2], dp[i-1])

print(max(dp))