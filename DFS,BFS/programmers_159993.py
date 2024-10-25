from collections import deque

def bfs(y, x, maps, target):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = deque([(y, x, 0)])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    # dfs에서는 출발점을 미리 방문 처리
    visited[y][x] = True

    while queue:
        ny, nx, count = queue.popleft()

        if maps[ny][nx] == target:
            return count

        for i in range(4):
            temp_y = ny + dy[i]
            temp_x = nx + dx[i]

            # 움직일 수 있는 곳이면
            if 0 <= temp_y < len(maps) and 0 <= temp_x < len(maps[0]):
                if maps[temp_y][temp_x] != "X" and visited[temp_y][temp_x] == False:
                    queue.append((temp_y, temp_x, count + 1))
                    # 여기서 방문 처리 해줘야한다
                    visited[temp_y][temp_x] = True
    return -1

def solution(maps):
    # count를 따로 지정하는거 활용! , count가 각 요소마다 따로 지정되어 최소일때 count만 딱 답으로 지정하면 됨
    # L을 찾은후에는 L이 새로운 시작점
    new_maps = []
    answer = 0
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                start = (y, x)

            if maps[y][x] == "L":
                lever = (y, x)

    # 먼저 레버가 있는 곳으로 가기
    to_lever = bfs(start[0], start[1], maps, "L")

    if to_lever == -1:
        answer = -1
    else:
        answer += to_lever
        to_exit = bfs(lever[0], lever[1], maps, "E")
        if to_exit == -1:
            answer = -1
        else:
            answer += to_exit

    return answer