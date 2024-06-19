import copy
import sys
N,B = map(int,sys.stdin.readline().split())

M = []
for _ in range(N):
    M.append(list(map(int,sys.stdin.readline().split())))

def solA (U,V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000
    return Z


def solB(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

    tmp = solB(A, B // 2)
    if B % 2:
        return solA(solA(tmp, tmp), A)
    else:
        return solA(tmp, tmp)

result = solB(M, B)
for r in result:
    print(*r)