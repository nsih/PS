#sys.stdin.readline()

from array import array
import sys

s = sys.stdin.readline().strip()
s2 = []

for i in range(ord("a"),ord("z")+1):
    s2.append(-1)
    for idx in range(len(s)):
        if chr(i) == s[idx] and s2[i-ord("a")] < 0:
            s2[i-ord("a")] = idx
            continue

for item in s2:
    print(item,end=' ')

'''
S = input()
ans = []
for i in range(97, 123):
    ans.append(str(S.find(chr(i))))
ans = ' '.join(ans)
print(ans)
'''