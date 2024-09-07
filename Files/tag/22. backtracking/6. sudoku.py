import sys
sys.setrecursionlimit(10000)


def checkRow(x, a):
    for i in range(9):
        if a == sudoku[i][x]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == sudoku[y][i]:
            return False
    return True

def checkRect(y, x, a):
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if a == sudoku[ny+i][nx+j]:
                return False
    return True

def Sol(y,x):
    if y == 9:
        return True
    if x == 9:
        return Sol(y+1,0)

    if sudoku[y][x] != 0:
        return Sol(y,x+1)

    for i in range(1,10):
        if checkRow(x,i) and checkCol(y,i) and checkRect(y,x,i):
            sudoku[y][x] = i

            if Sol(y, x+1):
                return True
            sudoku[y][x] = 0
    return False

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int,sys.stdin.readline().split())))

Sol(0,0)

for row in sudoku:
    print(' '.join(map(str,row)))