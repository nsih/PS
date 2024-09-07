import sys
input = sys.stdin.readline

lst = [0]*101

lst[1] = 1
lst[2] = 1
lst[3] = 1
lst[4] = 2
lst[5] = 2
lst[6] = 3
lst[7] = 4
lst[8] = 5
lst[9] = 7

for i in range(10, 101):
    lst[i] = lst[i - 1] + lst[i - 5]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(lst[N])