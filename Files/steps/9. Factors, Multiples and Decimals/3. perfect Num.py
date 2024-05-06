#a,b = map(int,sys.stdin.readline().split())

from array import array

import sys

while True:
    n = int(sys.stdin.readline())
    sum = 0
    factor = []
    factor.clear()

    if n == -1:
        break;

    for i in range(1,n):
        if n%i == 0:
            factor.append(i)
            sum += i
    if sum == n:
        print(n,end='')
        print(" = ",end='')
        for idx in range(len(factor)):
            if idx == len(factor)-1:
                print(factor[idx])
            else:
                print(factor[idx],end=' + ')

    else:
        print(n,end='')
        print(" is NOT perfect.")