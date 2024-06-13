import sys

n,m = map(int,sys.stdin.readline().split())

lst = [[0]*(n+1) for _ in range(n)]


for i in range(n):
    sum = 0
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1,n+1):
        sum += temp[j-1]
        lst[i][j] = sum

for _ in range(m):
    a1,a2,b1,b2 = map(int, sys.stdin.readline().split())
    sum = 0
    for i in range(a1-1,b1):
        sum += lst[i][b2] - lst[i][a2-1]

    print(sum)