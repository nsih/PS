def two_pointer(n, m, lst):
    left, right = 0, 0
    current_sum = 0

    min_length = float('inf')

    while right < n:
        current_sum += lst[right]

        right += 1

        while current_sum >= m:
            min_length = min(min_length, right - left)
            current_sum -= lst[left]
            left += 1

    if min_length != float('inf'):
        return min_length
    else:
        return 0


import sys

n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

result = two_pointer(n, m, lst)
print(result)