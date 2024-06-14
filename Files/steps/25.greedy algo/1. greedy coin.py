import sys

n,k = map(int,sys.stdin.readline().split())

coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

ans = 0
coin.reverse()

while k != 0:
    for i in coin:
        if i <= k:
            ans += k//i
            k = k%i
            break
print(ans)