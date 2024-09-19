graph = {1: [3], 2: [3], 3: [4], 4: [5, 6] ,5:[], 6:[]}

def recursive_dfs(node , visited = []):
    visited.append(node)
    for i in graph[node] :
        if i not in visited:
            visited = recursive_dfs(i,visited)
    return visited

def dfs(node):
    visited = []
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


print(dfs(1))

from collections import deque

def bfs(node):
    queue = deque([node])
    visited = [node]

    while queue:
        v = queue.popleft()
        for i in graph[v]: # for문의 위치가 dfs 와는 다름
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(bfs(1))
