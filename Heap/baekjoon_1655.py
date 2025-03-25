import sys
import heapq

n = int(sys.stdin.readline().strip())
max_heap = []
min_heap = []

for _ in range(n):
    number = int(sys.stdin.readline().strip())

    if not max_heap or number <= -max_heap[0]:
        heapq.heappush(max_heap, -number)
    else:
        heapq.heappush(min_heap, number)

    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    print(-max_heap[0])