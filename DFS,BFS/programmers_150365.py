from collections import deque
from copy import deepcopy

def solution(n, m, x, y, r, c, k):
    answer = ''
    answer_arr = []
    queue = deque([(0, x - 1, y - 1, [])])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    command = ["d", "u", "r", "l"]

    while queue:
        count, temp_x, temp_y, paths = queue.popleft()
        if count == k and temp_x == r - 1 and temp_y == c - 1:
            answer_arr.append(paths)
        elif count < k:
            for i in range(4):
                tx = temp_x + dx[i]
                ty = temp_y + dy[i]

                if 0 <= tx < n and 0 <= ty < m:
                    temp_paths = deepcopy(paths)
                    temp_paths.append(command[i])
                    queue.append((count + 1, tx, ty, temp_paths))

    answer_arr.sort()

    if len(answer_arr) == 0:
        answer = "impossible"
    else:
        answer = answer_arr[0]
        answer = "".join(answer)

    return answer