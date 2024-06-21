import sys

def sol(a,b,c):
    a = a%c
    ans = 1

    while b>0:
        if b%2 == 1:
            ans = (ans*a)%c

        b = b//2
        a = a**2 %c

    return ans