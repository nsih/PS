#a,b = map(int,sys.stdin.readline().split())

from array import array

import collections
import sys
x,y,w,h = map(int,sys.stdin.readline().split())
print (min(x,w-x,y,h-y))