#a,b = map(int,sys.stdin.readline().split())
#L = []
#L.extend(list(map(int,sys.stdin.readline().split())))
from array import array
import collections
import sys
a, b, c, d, e, f = map(int,sys.stdin.readline().split())
print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))
'''
ax + by = c
dx + ey = f

ad x + bd y = cd
ad x + ae y = fa

(bd-ae) y = cd-fa
'''