import sys

def two_pointer(lst,x):
    l = len(lst)
    cnt = 0

    left,right = 0,l-1

    while left < right:
        current_sum = lst[left] + lst[right]

        if current_sum == x:
            cnt +=1
            left +=1
            right -=1

        elif current_sum < x:
            left += 1

        else:
            right -= 1


    return cnt



n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

lst.sort()

print(two_pointer(lst,x))