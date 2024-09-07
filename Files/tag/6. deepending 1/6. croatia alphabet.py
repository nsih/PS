#sys.stdin.readline()

from array import array

import sys

cra = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().strip()

count = len(word)

for idx in range(len(word)):
    for idx2 in range(len(cra)):
        if word[idx:idx+3] == (cra[idx2]) and len((cra[idx2])) == 3:
            count -=2

        if word[idx:idx+2] ==(cra[idx2]) and word[idx-1:idx+2] not in cra  and len((cra[idx2])) == 2:
            count -=1

print(count)