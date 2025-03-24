import sys
from collections import deque
n, q = map(int,sys.stdin.readline().strip().split())

graph = dict()
questions = []
for i in range(1, n + 1):
    graph[i] = dict()

for _ in range(n - 1) :
    start,end,distance = map(int,sys.stdin.readline().strip().split())
    graph[end][start] = distance
    graph[start][end] = distance

for _ in range(q):
    k, v = map(int,sys.stdin.readline().strip().split())
    questions.append((k,v))

for key in graph.keys():
    visited = [False] * (n + 1)
    q = deque([])
    visited[key] = True

    for neighbor in graph[key].keys():
        q.append((neighbor, graph[key][neighbor]))
        visited[neighbor] = True

    while q:
        node, d = q.popleft()
        for next_key in graph[node].keys():
            if not visited[next_key]:
                usado = min(d, graph[node][next_key])
                visited[next_key] = True
                graph[key][next_key] = usado
                graph[next_key][key] = usado
                q.append((next_key,usado))

for question in questions:
    k,v = question
    answer = 0
    for key in graph[v].keys():
        if graph[v][key] >= k :
            answer += 1
    print(answer)