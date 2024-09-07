import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

rLst = lst[::-1]

dp = [1]*n
dp2 = [1]*n
for i in range(1,n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

        if rLst[i] > rLst[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2 = dp2[::-1]

r = []

for i in range(n):
    r.append(dp2[i]+dp[i]-1)

print(max(r))