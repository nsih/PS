h,m = map(int, input().split())

if m - 45 < 0:
    m  = m+15
    h = h-1
    if(h < 0):
        h = 23
else :
    m = m-45

print(h, m)