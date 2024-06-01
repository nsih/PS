import sys
sys.setrecursionlimit(10000)


def Score(team1,team2):
    sum1 = 0
    sum2 = 0

    for i in range(N//2):
        for j in range(N//2):
            if i < j:
                sum1 += st[team1[i]][team1[j]]
                sum1 += st[team1[j]][team1[i]]
    for i in range(N//2):
        for j in range(N//2):
            if i < j:
                sum2 += st[team2[i]][team2[j]]
                sum2 += st[team2[j]][team2[i]]

    return answer.append(abs(sum1-sum2))

def Sol(idx):
    if idx == N-1:
        return
    if len(team1) == N//2:
        for i in range(N):
            if not used[i]:
                team2.append(i)
        Score(team1,team2)
        #print(team1,team2)
        team2.clear()
        return

    for i in range(idx,N):
        if len(team1) == 0:
            if used[i] == False:
                used[i] = True
                team1.append(i)
                Sol(idx+1)
                used[i] = False
                team1.pop()
        else:
            if used[i] == False and i > team1[-1]:
                used[i] = True
                team1.append(i)
                Sol(idx+1)
                used[i] = False
                team1.pop()



N = int(sys.stdin.readline())
st = []
team1 = []
team2 = []
used = [False] * N
answer = []

for row in range(N):
    st.append(list(map(int,sys.stdin.readline().split())))

Sol(0)

print(min(answer))