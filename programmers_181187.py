from collections import deque

def solution(r1, r2):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    answer = 0
    visited = [[0] * (r2 + 1) for _ in range(r2 + 1)]
    stack = [(r1, 1)]

    while stack:
        x, y = stack.pop()

        if visited[x][y] == 0:
            answer += 1
            visited[x][y] = 1
            for i in range(4):
                tmp_x = x + dx[i]
                tmp_y = y + dy[i]

                if (tmp_x ** 2 + tmp_y ** 2 >= r1 ** 2) and (tmp_x ** 2 + tmp_y ** 2 <= r2 ** 2) and (tmp_x > 0) and (
                        tmp_y > 0):
                    stack.append((tmp_x, tmp_y))

    return 4 * answer + 4 * (r2 - r1 + 1)