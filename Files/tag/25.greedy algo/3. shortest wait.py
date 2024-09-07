import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
sumLst = []

sum = 0
for i in lst:
    sum += i
    sumLst.append(sum)


sum = 0
for i in sumLst:
    sum += i

print(sum)