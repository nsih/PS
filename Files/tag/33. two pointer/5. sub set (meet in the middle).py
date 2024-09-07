def count_subsets(weights, capacity):
    n = len(weights)
    mid = n//2

    #
    left_part = weights[:mid]
    left_sums = []
    right_part = weights[mid:]
    right_sums = []

    #모든 부분집합의 합구하는 함수
    def subset_sum(arr, subset_sums):
        n = len(arr)
        for i in range(1 << n): #2^n 부분집합 생성
            sum_val = 0
            for j in range(n):
                if i & (1 << j): #i의 j번째 비트가 1이면 arr[j]에 포함
                    sum_val += arr[j]
            subset_sums.append(sum_val)

    #부분집합들의 합 구하고 정렬
    subset_sum(left_part,left_sums)
    subset_sum(right_part,right_sums)

    left_sums.sort()
    right_sums.sort()

    cnt = 0
    left,right = 0, len(right_sums) - 1

    while left < len(left_sums) and right >= 0:
        if left_sums[left] + right_sums[right] <= capacity:
            cnt += right + 1
            left += 1
        else:
            right -= 1

    return cnt


import sys

n,c = map(int, sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

print(count_subsets(lst,c))