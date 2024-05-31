import sys

def CheckQ(x,y,lst):
    for i in range(len(lst)):
        if lst[i] == y or abs(lst[i]-y) == abs( i - x):
            return False
    return True

def Queen(x,N):
    global answer

    if N%2 == 0:
        if x == N:
            answer += 2
            return

        for y in range(N):
            if CheckQ(x,y,lst):
                lst.append(y)

                if lst[0] >= N // 2:
                    return

                Queen(x+1,N)
                lst.pop()
    else:
        if x == N:
            if lst[0] == N//2:
                answer += 1
            else:
                answer += 2
            return

        for y in range(N):
            if CheckQ(x, y, lst):
                lst.append(y)

                if lst[0] > N // 2:
                    return

                Queen(x + 1, N)
                lst.pop()


N = int(sys.stdin.readline())
answer = 0
lst = []

Queen(0,N)
print(answer)