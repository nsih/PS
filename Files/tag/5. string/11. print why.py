#sys.stdin.readline()

from array import array
import sys

count = 0
while (1):
    words = sys.stdin.readline()
    print(words,end='')
    count += 1

    if words == "\n" or count > 100:
        break;