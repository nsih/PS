import sys

n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

sumLst = [0]

r = [0]*m

temp = 0
for i in lst:
    temp += i
    r[temp % m] += 1

res = r[0]
for i in range(m):
    res += r[i] * (r[i]-1) // 2

print(res)