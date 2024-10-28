from collections import deque

def solution(maps):
    answer = 0
    start = (0, 0)
    end = (len(maps) - 1, len(maps[0]) - 1)
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        y, x, count = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny == len(maps) - 1 and nx == len(maps[0]) - 1:
                return count + 1
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] != 0:
                if not visited[ny][nx]:
                    queue.append((ny, nx, count + 1))
                    visited[ny][nx] = True

    return -1