#sys.stdin.readline()

from array import array

import sys

N = int(sys.stdin.readline())

GN = N;


for _ in range(N):
    abc = [0] * 26
    str = sys.stdin.readline().strip()

    for i in range(len(str)):
        if i == 0:
            abc[ord(str[i]) - ord("a")] += 1
        else:
            if str[i] != str[i-1]:
                if abc[ord(str[i]) - ord("a")] != 1:
                    abc [ord(str[i])-ord("a")] += 1
                else:
                    GN -= 1
                    break;

print(GN)