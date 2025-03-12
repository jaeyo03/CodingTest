import sys
import heapq

n, m, x = map(int,sys.stdin.readline().split())

roads = dict()

for _ in range(m) :
    start, end, distance = map(int,sys.stdin.readline().split())
    if roads.get(start):
        roads[start].append((end, distance))
    else :
        roads[start] = [(end, distance)]

max_time = 0

def dijkstra(graph, start, n):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_time, current_node  = heapq.heappop(heap)
        if current_time > distances[current_node]:
            continue

        for next_node, weight in graph[current_node]:
            new_distance = current_time + weight
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(heap, (new_distance, next_node))

    return distances

for student in range(1,n+1) :
    total_time = dijkstra(roads, student, n)[x] + dijkstra(roads, x, n)[student]
    if total_time > max_time :
        max_time = total_time

print(max_time)