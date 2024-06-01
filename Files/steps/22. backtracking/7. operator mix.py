import sys
sys.setrecursionlimit(10000)

def C():
    C = lst1[0]
    for i in range(0,N):
        if i != 0:
            if lst4[i-1] == 0:
                C += lst1[i]
            elif lst4[i-1] == 1:
                C -= lst1[i]
            elif lst4[i-1] == 2:
                C *= lst1[i]
            elif lst4[i-1] == 3:
                C = int(C/lst1[i])
    return C

def Sol():
    if len(lst4) == N-1:
        answer.append(C())
        return

    for i in range(N-1):
        if not used[i]:
            used[i] = True
            lst4.append(lst3[i])
            Sol()
            lst4.pop()
            used[i] = False

N = int(sys.stdin.readline())
lst1 = list(map(int,sys.stdin.readline().split()))
lst2 = list(map(int,sys.stdin.readline().split()))
lst3 = []
lst4 = []

answer = []

for i in range(4):
    lst3.extend([i] * lst2[i])

used = [False] * len(lst3)
Sol()

print(max(answer))
print(min(answer))