import sys

sumW = 0
sumB = 0

def dLst(arr):
    global sumB
    global sumW

    slen = len(arr)

    if slen == 1:
        if arr[0][0] == 0:
            sumW += 1
        else:
            sumB += 1
        return

    is_uniform = all(arr[i][j] == arr[0][0] for i in range(slen) for j in range(slen))

    if is_uniform:
        if arr[0][0] == 0:
            sumW += 1
        else:
            sumB += 1

    else:
        half = slen // 2
        top_left = [row[:half] for row in arr[:half]]
        top_right = [row[half:] for row in arr[:half]]
        bottom_left = [row[:half] for row in arr[half:]]
        bottom_right = [row[half:] for row in arr[half:]]

        dLst(top_left)
        dLst(top_right)
        dLst(bottom_left)
        dLst(bottom_right)

    return


n = int(sys.stdin.readline())
sLst = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]

dLst(sLst)

print(sumW)
print(sumB)