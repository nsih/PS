import sys
import heapq

def dijkstra(start, end):
    if start == end:
        path = []
        path.append(start)
        return (0, [start]),path

    min_time = [(INF, 0)] * (100000 + 1)
    min_time[start] = (0, 0)

    # 우선순위 큐
    Q = [(0, start)]

    while Q:
        current_time, current_position = heapq.heappop(Q)

        if min_time[current_position][0] < current_time:
            continue

        def update_position(next_position, time_cost):
            if 0 <= next_position <= 100000:
                new_time = current_time + time_cost
                if new_time < min_time[next_position][0]:
                    min_time[next_position] = (new_time, current_position)
                    heapq.heappush(Q, (new_time, next_position))

        update_position(current_position - 1, 1)
        update_position(current_position + 1, 1)

        update_position(current_position * 2, 1)

    # backtracking
    path = []
    path.append(end)
    s = end
    while min_time[s][1]:
        path.append(min_time[s][1])
        s = min_time[s][1]
    path.reverse()

    return min_time[end], path

INF = sys.maxsize
N, K = map(int, sys.stdin.readline().split())

result, path = dijkstra(N, K)
print(result[0])
print(*path)