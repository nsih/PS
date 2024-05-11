#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
y,x = map(int,sys.stdin.readline().split())

matrix = [sys.stdin.readline().strip() for line in range(y)]

count1 = 0
for i in range(y):
    for j in range(x):
        if i%2 == 0 and j%2 == 0 and matrix[i][j] == "B":
            count1 += 1
        elif i%2 == 0 and j %2 != 0 and matrix[i][j] == "W":
            count1 += 1
        elif i%2 != 0 and j%2 == 0 and matrix[i][j] == "W":
            count1 += 1
        elif i%2 != 0 and j%2 != 0 and matrix[i][j] == "B":
            count1 += 1

count2 = 0
for i in range(y):
    for j in range(x):
        if i%2 == 0 and j%2 == 0 and matrix[i][j] == "W":
            count2 += 1
        elif i%2 == 0 and j %2 != 0 and matrix[i][j] == "B":
            count2 += 1
        elif i%2 != 0 and j%2 == 0 and matrix[i][j] == "B":
            count2 += 1
        elif i%2 != 0 and j%2 != 0 and matrix[i][j] == "W":
            count2 += 1

print(count1,count2)