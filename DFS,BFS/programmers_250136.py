# 효율성 개선 필요
def my_solution(land):
    answer = 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for x in range(len(land[0])):
        count = 0
        visited = set()
        for y in range(len(land)):
            # 시작점은 y,x
            stack = [(y, x)]
            while stack:
                ny, nx = stack.pop()
                if (ny, nx) in visited or land[ny][nx] == 0:
                    continue
                else:
                    visited.add((ny, nx))
                    for i in range(4):
                        temp_y = ny + dy[i]
                        temp_x = nx + dx[i]
                        if 0 <= temp_x < len(land[0]) and 0 <= temp_y < len(land):
                            if land[temp_y][temp_x] == 1:
                                stack.append((temp_y, temp_x))
        count = len(visited)
        if count > answer:
            answer = count

    return answer


# 지피티 답
def solution(land):
    from collections import deque, defaultdict

    n = len(land)
    m = len(land[0])

    # 방향 벡터 (상, 하, 좌, 우)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    # 석유 덩어리 라벨링 및 크기 저장
    component_labels = [[0] * m for _ in range(n)]
    component_sizes = defaultdict(int)
    label = 1  # 라벨은 1부터 시작

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and component_labels[y][x] == 0:
                # BFS로 석유 덩어리 탐색
                queue = deque()
                queue.append((y, x))
                component_labels[y][x] = label
                size = 1  # 현재 덩어리의 크기

                while queue:
                    ny, nx = queue.popleft()
                    for i in range(4):
                        temp_y = ny + dy[i]
                        temp_x = nx + dx[i]
                        if 0 <= temp_y < n and 0 <= temp_x < m:
                            if land[temp_y][temp_x] == 1 and component_labels[temp_y][temp_x] == 0:
                                component_labels[temp_y][temp_x] = label
                                queue.append((temp_y, temp_x))
                                size += 1
                component_sizes[label] = size
                label += 1

    # 각 열에 대해 겹치는 덩어리의 크기 합산
    answer = 0
    for x in range(m):
        seen_labels = set()
        for y in range(n):
            clabel = component_labels[y][x]
            if clabel != 0:
                seen_labels.add(clabel)
        total_oil = sum(component_sizes[cl] for cl in seen_labels)
        answer = max(answer, total_oil)

    return answer