import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

R = []
G = []
B = []

for i in range(n):
    lst = list(map(int,sys.stdin.readline().split()))

    R[i] = lst[0]
    G[i] = lst[1]
    B[i] = lst[2]

for i in range(n):
    