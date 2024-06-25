import sys

numM = 0
num0 = 0
num1 = 0

def sol(arr):
    global numM
    global num0
    global num1

    slen = len(arr)

    if slen == 1:
        if arr[0][0] == -1:
            numM += 1
        elif arr[0][0] == 0:
            num0 += 1
        else:
            num1 += 1
        return

    is_uniform = all(arr[i][j] == arr[0][0] for i in range(slen) for j in range(slen))

    if is_uniform:
        if arr[0][0] == -1:
            numM += 1
        elif arr[0][0] == 0:
            num0 += 1
        else:
            num1 += 1
        return

    else:
        D1 = slen // 3
        D2 = (slen // 3) * 2

        top_left = [row[:D1] for row in arr[:D1]]
        top_mid = [row[D1:D2] for row in arr[:D1]]
        top_right = [row[D2:] for row in arr[:D1]]
        mid_left = [row[:D1] for row in arr[D1:D2]]
        mid_mid = [row[D1:D2] for row in arr[D1:D2]]
        mid_right = [row[D2:] for row in arr[D1:D2]]
        bottom_left = [row[:D1] for row in arr[D2:]]
        bottom_mid = [row[D1:D2] for row in arr[D2:]]
        bottom_right = [row[D2:] for row in arr[D2:]]

        sol(top_left)
        sol(top_mid)
        sol(top_right)
        sol(mid_left)
        sol(mid_mid)
        sol(mid_right)
        sol(bottom_left)
        sol(bottom_mid)
        sol(bottom_right)
    return


n = int(sys.stdin.readline())
sLst = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]

sol(sLst)

print(numM)
print(num0)
print(num1)