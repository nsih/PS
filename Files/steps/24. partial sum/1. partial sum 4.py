import sys

n,m = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

sumLst = [0]

temp = 0
for i in lst:
    temp += i
    sumLst.append(temp)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    print(sumLst[b]-sumLst[a-1])