#sys.stdin.readline()

from array import array
import sys

word = sys.stdin.readline().strip()

arr = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

time = 0

for item in word:
    time += arr[ord(item)-ord("A")]

print(time)