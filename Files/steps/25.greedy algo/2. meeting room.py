import sys

n = int(sys.stdin.readline())
t = []

for i in range(n):
    t.append(list(map(int,sys.stdin.readline().split())))

t.sort(key = lambda  x: (x[1],x[0]))
cnt = 1

end = t[0][1]

for i in range(1,n):
    if t[i][0] >= end:
        cnt += 1
        end = t[i][1]

print(cnt)