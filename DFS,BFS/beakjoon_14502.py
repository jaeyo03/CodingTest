import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def spread_virus(n,m,graph):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    start_points = []
    visited = [[False] * m] * n

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2 :
                start_points.append((i,j))

    while start_points:
        y,x = start_points.pop()
        if not visited[y][x]:
            visited[y][x] = True
            for inx in range(4):
                next_y = y + dy[inx]
                next_x = x + dx[inx]
                if 0 <= next_y < n and 0 <= next_x < m and graph[next_y][next_x] == 0:
                    graph[next_y][next_x] = 2
                    start_points.append((next_y,next_x))

    return graph

for i in spread_virus(n,m,graph):
    print(i)

for possible_case in combinations(range(n * m), 3):
    for point in possible_case:
        y = point // m
        x = point % m
        if graph[y][x] == 2 or graph[y][x] == 1 :
            break

        graph[y][x] = 1
