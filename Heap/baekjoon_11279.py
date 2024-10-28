import sys
import heapq

n = int(sys.stdin.readline())
arr = []
heapq.heapify(arr)

for _ in range(n):
    number = int(sys.stdin.readline())

    if number > 0:
        heapq.heappush(arr, -number)

    else:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))