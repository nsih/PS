def two_pointer(n, lst):
    lst.sort()

    left, right = 0, n - 1
    closest_sum = float('inf')
    result = (0, 0)

    while left < right:
        current_sum = lst[left] + lst[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (lst[left], lst[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return result


import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

result = two_pointer(n, lst)
print(result[0], result[1])