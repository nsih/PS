#sys.stdin.readline()

from array import array
import sys

s = sys.stdin.readline().split()

print(len(s))


'''
import sys

st = sys.stdin.readline().strip()

addable = True
count = 0

for idx in range(0, len(st)):
    if addable and st[idx] != " ":
        count += 1
        addable = False

    elif addable == False and st[idx] == " ":
        addable = True

    else:
        continue

print(count)
'''