import sys

def sol(a,b,c):
    a = a%c
    ans = 1

    while b>0:
        if b%2 == 1:
            ans = (ans*a) % c

        b = b // 2
        a = a**2 % c

    return ans

lst = list(map(int,sys.stdin.readline().split()))
print(sol(lst[0], lst[1], lst[2]))