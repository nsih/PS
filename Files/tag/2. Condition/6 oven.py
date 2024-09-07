h,m = map(int, input().split())
t = int(input())

if (m + t) >= 60:
    h += (m+t) // 60
    m = (m+t) % 60
    if(h > 23):
        h = h-24
else:
    m = m+t

print(h, m)