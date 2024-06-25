import sys

K,N = map(int,sys.stdin.readline().split())

lst = []
sum = 0

for _ in range(K):
    lst.append(int(sys.stdin.readline()))
    sum += lst[-1]

def sol(lst, N):
    left, right = 1, max(lst)

    while left <= right:
        mid = (left+right) // 2

        x = 0
        for i in range(len(lst)):
            x += lst[i]//mid

        if x >= N:  #k이상 나오면
            result = mid
            left = mid + 1 #최대값을 찾으러 간다.
        else:   #k개가 안나오면 (너무 길게 잘랐으면)
            right = mid - 1

    return result

print(sol(lst,N))