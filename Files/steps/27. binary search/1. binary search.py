import sys

N = int(sys.stdin.readline())
nLst = list(map(int, sys.stdin.readline().split()))
nLst.sort()

M = int(sys.stdin.readline())
mLst = list(map(int, sys.stdin.readline().split()))

def sol(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid-1

    return 0


for i in mLst:
    print(sol(nLst,i))