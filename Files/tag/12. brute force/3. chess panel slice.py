#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys

def countPaint(a):
    count = 0
    for i in range(8):
        for j in range(8):
            if i%2 == 0 and j%2 == 0 and a[i][j] == "B":
                count += 1
            elif i%2 == 0 and j %2 != 0 and a[i][j] == "W":
                count += 1
            elif i%2 != 0 and j%2 == 0 and a[i][j] == "W":
                count += 1
            elif i%2 != 0 and j%2 != 0 and a[i][j] == "B":
                count += 1
    if count > 32:
        count = 64-count
    return count

###

y,x = map(int,sys.stdin.readline().split())

matrix = [sys.stdin.readline().strip() for line in range(y)]
change = []
for i in range(len(matrix) - 8+1):
    for j in range(len(matrix[0]) - 8+1):
        small_array = [row[j:j+8] for row in matrix[i:i+8]]
        change.append(countPaint(small_array))
print(min(change))