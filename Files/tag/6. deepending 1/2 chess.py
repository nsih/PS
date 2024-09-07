#sys.stdin.readline()

from array import array
import sys

chess = [1,1,2,2,2,8]

myChess = list(map(int,sys.stdin.readline().split()))

for idx in range(len(myChess)):
    print(chess[idx]-myChess[idx],end=' ')