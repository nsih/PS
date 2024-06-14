import sys

n,k = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

sumLst = [0]

temp = 0
for i in lst:
    temp += i
    sumLst.append(temp)

resultLst = []

for i in range(len(sumLst)-k):
    resultLst.append(sumLst[i+k] - sumLst[i])

print(max(resultLst))