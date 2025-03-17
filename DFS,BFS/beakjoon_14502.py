import sys
from itertools import combinations
from copy import deepcopy

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

def spread_virus(n, m, graph):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    stack = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 :
                stack.append((i, j))

    while stack:
        y, x = stack.pop()
        for inx in range(4):
            ny, nx = y + dy[inx], x + dx[inx]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = 2
                stack.append((ny, nx))
    return graph

for walls in combinations(range(n * m), 3):
    count = 0
    temp_graph = deepcopy(graph)
    is_valid = True
    for wall in walls:
        y, x = wall // m, wall % m
        if temp_graph[y][x] != 0:
            is_valid = False
            break
        temp_graph[y][x] = 1
    if not is_valid:
        continue

    virus_spread_graph = spread_virus(n, m, temp_graph)

    for i in range(n):
        for j in range(m):
            if virus_spread_graph[i][j] == 0:
                count += 1

    if count > answer:
        answer = count

    answer = max(answer, count)

print(answer)