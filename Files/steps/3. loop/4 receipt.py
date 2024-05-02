#a,b,c = map(int, input().split())

total = int(input())
n = int(input())
sum = 0

for i in range(1, n+1):
    a, b = map(int, input().split())
    sum += a*b

if sum == total:
    print("Yes")
else:
    print("No")