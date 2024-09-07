#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys

N, M = map(int,sys.stdin.readline().split())

card = []

card.extend(list(map(int,sys.stdin.readline().split())))

max = 0
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if card[i]+card[j]+card[k] > max and card[i]+card[j]+card[k] <= M:
                max = card[i]+card[j]+card[k]

print(max)