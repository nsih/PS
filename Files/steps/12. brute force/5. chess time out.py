import sys

def countPaint(a,k):
    count = 0
    for i in range(k):
        for j in range(k):
            if i%2 == 0 and j%2 == 0 and a[i][j] == "B":
                count += 1
            elif i%2 == 0 and j %2 != 0 and a[i][j] == "W":
                count += 1
            elif i%2 != 0 and j%2 == 0 and a[i][j] == "W":
                count += 1
            elif i%2 != 0 and j%2 != 0 and a[i][j] == "B":
                count += 1
    if count > (k*k)//2:
        count = (k*k)-count
    return count

###

n, m, k = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline().strip() for _ in range(n)]


change = []

for i in range(len(lst) - k + 1):
    for j in range(len(lst[0]) - k + 1):
        small_array = [row[j:j+k] for row in lst[i:i+k]]
        #print(small_array)
        change.append(countPaint(small_array,k))
print(min(change))