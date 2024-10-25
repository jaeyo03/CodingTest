def solution(board):
    from collections import deque

    n = len(board)
    m = len(board[0])

    grid = [list(row) for row in board]

    # Find the starting position 'R' and goal position 'G'
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((start[0], start[1], 0))  # (row, col, moves)

    visited = [[False]*m for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, moves = queue.popleft()

        if (x, y) == goal:
            return moves

        for dx, dy in directions:
            nx, ny = x, y

            # Slide in the direction until hitting an obstacle or edge
            while True:
                tx = nx + dx
                ty = ny + dy

                # Check for edge of the board
                # break를 통해, 만약 이동한 값이 맵 안에 존재하지 않는다면 밑에서 temp 값을 nx,ny에 지정하지 않음!
                # 결국 D 에 부딪히거나 벽에 부딪힌 상황인거임
                if not (0 <= tx < n and 0 <= ty < m):
                    break

                # Check for obstacle
                if grid[tx][ty] == 'D':
                    break

                nx, ny = tx, ty

            # If new position has not been visited
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1
