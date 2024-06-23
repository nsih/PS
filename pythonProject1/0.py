import sys

N,M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

def sol(lst, M):
    row, high = 0, max(lst)

    while row <= high:
        mid = (row+high) // 2

        x = 0
        for i in range(N):
            if lst[i] - mid > 0:
                x += lst[i]-mid

        if x >= M:  #필요한 양보다 자른게 많으면
            result = mid
            row = mid + 1   #더 높게 잘라본다

        else:
            high = mid - 1  #필요한 양을 못채우면 낮춰본다.

    return result

print(sol(lst,M))