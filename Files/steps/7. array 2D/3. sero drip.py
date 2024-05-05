#sys.stdin.readline()

from array import array

import sys

matrix = [list(sys.stdin.readline().strip()) for _ in range(5)]
maxRow = 0
for row in matrix:
    if len(row) > maxRow:
        maxRow = len(row)
for j in range(maxRow):
    for i in range(5):
        if len(matrix[i]) <= j:
            print("",end='')
        else:
            print(matrix[i][j],end='')