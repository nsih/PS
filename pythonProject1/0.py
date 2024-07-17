def two_pointer(n,c, lst):
    left, right = 0, 0
    current_sum = 0

    cnt = 0

    while right < len(lst):
        current_sum += lst[right]
        right += 1

        while current_sum >= c:
            cnt += 1

            current_sum -= lst[left]
            left += 1

    return cnt + 1

import sys

n,c = map(int, sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

print(two_pointer(n,c,lst))