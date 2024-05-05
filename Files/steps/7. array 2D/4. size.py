#sys.stdin.readline()

from array import array

import sys

matrix = [[0 for _ in range(100)] for _ in range(100)]
N = int(sys.stdin.readline())

for _ in range(N) :
    a,b = map(int,sys.stdin.readline().split())

    for i in range(b,b+10):
        for j in range(a,a+10):
            matrix[i][j] += 1

result = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] >= 1:
            result +=1

print(result)