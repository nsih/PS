#sys.stdin.readline()

from array import array

import sys


matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max = 0
p = [0,0]

for i in range(9):
    for j in range(9):
        if max < matrix[i][j]:
            max = matrix[i][j]
            p = [i,j]

print(max)
print(p[0]+1,p[1]+1)