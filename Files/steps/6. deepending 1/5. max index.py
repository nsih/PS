#sys.stdin.readline()

from array import array

import sys

apb = [0]*26

word = sys.stdin.readline().strip()

for item in word:
    if ord(item) >= ord("a"):
        apb[ ord(item) - ord("a") ] += 1

    else:
        apb[ord(item) - ord("A")] += 1

count = 0
for item in apb:
    if item == max(apb):
        count += 1

if count == 1:
    print(chr(apb.index(max(apb))+65) )
else:
    print("?")