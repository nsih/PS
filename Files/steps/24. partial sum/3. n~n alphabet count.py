import sys

S = sys.stdin.readline().rstrip()
count = {0 : [0] * 26}
for i, ch in enumerate(S):
    count[i + 1] = count[len(count) - 1][:]
    count[i + 1][ord(ch) - 97] += 1
print(count)

q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    a,l,s = map(str,sys.stdin.readline().split())
    l = int(l)
    s = int(s)

    answer = count[int(s)+1][ord(a)-97]-count[int(l)][ord(a)-97]
    print(answer)