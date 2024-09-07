import sys

n = int(sys.stdin.readline())
cLst = list(map(int,sys.stdin.readline().split())) #도시간거리
oLst = list(map(int,sys.stdin.readline().split())) #기름 값


coLst = [oLst[0]]

for i in range(1,len(oLst)):
    if coLst[-1] < oLst[i]:
        coLst.append(coLst[-1])
    else:
        coLst.append(oLst[i])

ans = 0
for i in range(len(coLst)-1):
    ans += coLst[i] * cLst[i]

print(ans)