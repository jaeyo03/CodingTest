from collections import deque

def solution(x, y, n):
    # bfs 이용
    queue = deque([(x, 0)])
    visited = [0] * 1000001  # bfs에서는 시간복잡도를 위해 방문한거 항상 체크하자
    visited[x] = 1

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        temp1 = current + n
        temp2 = current * 2
        temp3 = current * 3
        temp_arr = [temp1, temp2, temp3]

        for t in temp_arr:
            if t <= y and visited[t] == 0:
                visited[t] = 1
                queue.append((t, count + 1))

    return -1