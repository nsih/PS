def find_LIS(n, lst):
    import bisect

    if n == 0:
        return (0, [])

    lis = []
    prev_index = [-1] * n
    index_at = [0] * n

    for i in range(n):
        # lst[i]의 lis에서의 위치 pos
        pos = bisect.bisect_left(lis, lst[i])

        #삽입
        if pos < len(lis):
            lis[pos] = lst[i]
        else:
            lis.append(lst[i])

        # 이전 요소의 인덱스를 기록
        index_at[pos] = i
        if pos > 0:
            prev_index[i] = index_at[pos - 1]
        else:
            prev_index[i] = -1

    # LIS 길이 및 수열 복원
    lis_len = len(lis)
    lis_seq = []
    k = index_at[lis_len - 1]

    while k != -1:
        lis_seq.append(lst[k])
        k = prev_index[k]

    lis_seq.reverse()

    return (lis_len, lis_seq)


import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

length, seq = find_LIS(n, lst)

print(length)
print(*seq)