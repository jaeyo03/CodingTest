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


## 정답 풀이
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
edges = []
for _ in range(n - 1):
    p, q_, r = map(int, input().split())
    edges.append((r, p, q_))
edges.sort(reverse=True)  # 가중치 내림차순 정렬

queries = []
for i in range(q):
    k, v = map(int, input().split())
    queries.append((k, v, i))
queries.sort(reverse=True)  # 임계값 내림차순 정렬

# Union-Find (DSU 구조) 구조 초기화
parent = [i for i in range(n+1)]
size = [1] * (n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

# 쿼리 처리
answers = [0] * q
edge_index = 0

for k, v, idx in queries:
    # 현재 쿼리의 임계값 k 이상인 간선을 모두 union
    while edge_index < len(edges) and edges[edge_index][0] >= k:
        _, a, b = edges[edge_index]
        union(a, b)
        edge_index += 1
    # 정점 v와 연결된 컴포넌트의 크기에서 자신을 빼줌
    answers[idx] = size[find(v)] - 1

for ans in answers:
    print(ans)