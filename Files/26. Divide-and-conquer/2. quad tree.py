import sys

def quadTree(arr):
    slen = len(arr)

    if slen == 1:
        print(arr[0][0],end='')
        return

    is_uniform = all(arr[i][j] == arr[0][0] for i in range(slen) for j in range(slen))

    if is_uniform:
        print(arr[0][0],end='')

    else:
        half = slen // 2
        top_left = [row[:half] for row in arr[:half]]
        top_right = [row[half:] for row in arr[:half]]
        bottom_left = [row[:half] for row in arr[half:]]
        bottom_right = [row[half:] for row in arr[half:]]

        print('(',end='')
        quadTree(top_left)
        quadTree(top_right)
        quadTree(bottom_left)
        quadTree(bottom_right)
        print(')', end='')

    return


n = int(sys.stdin.readline())
sLst = []

for _ in range(n):
    line = sys.stdin.readline().strip()
    sLst.append(list(map(int, list(line))))


quadTree(sLst)