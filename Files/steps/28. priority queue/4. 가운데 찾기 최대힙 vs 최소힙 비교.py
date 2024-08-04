import sys
import heapq

N = int(sys.stdin.readline())

#heappop = 최소값 꺼냄

leftHeap = []   #최대를 꺼내기 위해 -로 저장
rightHeap = []  #최소를 꺼내기 위해 +로 저장
for _ in range(N):
    m = int(sys.stdin.readline())

    #최대값 빼내는 힙
    heapq.heappush(leftHeap, -m)

    #leftHeap의 최대 값이 right의 최소값보다 크면 rightheap으로
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))

    #
    if len(leftHeap) > len(rightHeap) + 1:
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))

    elif len(rightHeap) > len(leftHeap):
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))

    #print
    if len(leftHeap) >= len(rightHeap):
        print(-leftHeap[0])
    else:
        print(rightHeap[0])