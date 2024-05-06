#sys.stdin.readline()

from array import array

import sys

T = int( sys.stdin.readline().strip())

for _ in range(T):
    m = int(sys.stdin.readline().strip())

    if m // 25 >= 1:
        print(m // 25, end=' ')
    else:
        print("0", end=' ')
    m = m % 25

    if m//10 >= 1:
        print(m//10,end=' ')
    else:
        print("0",end=' ')
    m = m%10

    if m//5 >= 1:
        print(m//5,end=' ')
    else:
        print("0",end=' ')
    m = m%5

    print(m)