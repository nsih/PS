import select
from array import array
import collections
import math
from functools import reduce
from collections import deque
import math
from collections import Counter
import sys

def CheckQ(x,y,lst):
    itemX = 0
    for i in range(len(lst)):
        if lst[i] == y or abs(lst[i]-y) == abs(i - x):
            return False
        itemX += 1
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
            if lst[0] == round(N / 2):
                answer += 1
            else:
                answer += 2
            return

        for y in range(N):
            if CheckQ(x, y, lst):
                lst.append(y)

                if lst[0] > round(N / 2):
                    lst.pop()
                    return


                Queen(x + 1, N)
                lst.pop()


N = int(sys.stdin.readline())
answer = 0
lst = []
Queen(0,N)
print(answer)
'''
def KQ(y, x, lst):
    for item in lst:
        if x == item[1] or y == item[0] or abs(x - item[1]) == abs(y - item[0]):
            return False
    return True

def Queen(y, N, lst):
    global answer
    if y == N:
        answer += 1
        return

    for x in range(N):
        if KQ(y, x, lst):
            lst.append((y, x))
            Queen(y + 1, N, lst)
            lst.pop()

N = int(sys.stdin.readline())
answer = 0
lst = []

Queen(0, N, lst)
print(answer)
'''
'''
퀸 좌표 리스트

함수
y,x좌표의 퀸이 놓아진 퀸을 못잡는지 체크
잡힐 수 있으면 놓지말고 진행해야겠지?
N개 다 놓으면 마지막꺼 하나 씩 빼고 재귀가 알아서 해주겠지?
'''