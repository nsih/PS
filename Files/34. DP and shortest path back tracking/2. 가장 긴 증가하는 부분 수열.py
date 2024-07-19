def find_LIS(n,lst):
    if n == 0:
        return(0,[])

    #len
    dp = [1] * n
    prev = [-1] * n

    for i in range(1,n):
        for j in range(i):
            #lst[i]가 오름차수이고, j로 끝나는 수열에서 더했을때 길이가 길면
            if lst[j] < lst[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j]+1
                prev[i] = j

    #len
    lis_len = max(dp)
    lis_end_index = dp.index(lis_len)


    #back tracking
    lis_seq = []
    currentIDX = lis_end_index

    while currentIDX != -1:
        lis_seq.append(lst[currentIDX])
        currentIDX = prev[currentIDX]

    lis_seq.reverse()

    return(lis_len,lis_seq)


    return


import sys
import heapq

INF = sys.maxsize

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

len,seq = find_LIS(n,lst)

print(len)
print(*seq)

