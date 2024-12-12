from collections import deque

def solution(n, edge):
    answer = 0
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([(1, 0)])  # 노드 번호, 이동 거리
    visited = [0] * 20002  # visited를 이렇게 index로 해주는게 빠르다, visited = [] 이건 느림
    visited_with_length = [(1, 0)]
    visited[1] = 1

    # 최단 거리라서 bfs로 접근해야함
    while queue:
        node, length = queue.popleft()
        for w in graph[node]:
            if visited[w] == 0:
                visited[w] = 1
                visited_with_length.append((w, length + 1))
                queue.append((w, length + 1))

    visited_with_length.sort(key=lambda x: x[1], reverse=True)
    max_length = visited_with_length[0][1]

    for v in visited_with_length:
        if v[1] == max_length:
            answer += 1

    return answer