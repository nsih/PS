#sys.stdin.readline()

from array import array
import sys

a = int(sys.stdin.readline())

arr = array('i', map(int,sys.stdin.readline().split()))

element = int(sys.stdin.readline())
count = 0

for i in arr:
    if i == element:
        count += 1
print(count)

'''
import sys

a = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

element = int(sys.stdin.readline())

print(arr.count(element))
'''