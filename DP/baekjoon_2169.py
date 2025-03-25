import sys
from collections import deque
from copy import deepcopy

n, m = map(int, sys.stdin.readline().strip().split())
graph = []
answer = 0

for _ in range(n) :
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

start_y = 0
start_x = 0
count = graph[start_y][start_x]
visited = [[False] * m for _ in range(n)]
visited[start_y][start_x] = True
queue = deque([(start_y, start_x, count, visited)])

dy = [0,0,1]
dx = [1,-1,0]

while queue:
    y, x, count, visited = queue.popleft()

    if y == n - 1 and x == m - 1:
        if count > answer:
            answer = count
        continue

    for i in range(3) :
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < n and 0 <= next_x < m and not visited[next_y][next_x]:
            new_visited = deepcopy(visited)
            new_visited[next_y][next_x] = True
            new_count = count + graph[next_y][next_x]
            queue.append((next_y, next_x, new_count, new_visited))

print(answer)


# 답
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 충분히 작은 음의 값보다 작은 값으로 초기화 (문제에 따라 INF 값은 조정)
NEG_INF = -10 ** 9
dp = [[NEG_INF] * m for _ in range(n)]

# 첫 행은 왼쪽에서 오른쪽으로 누적 합
dp[0][0] = grid[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + grid[0][j]

# 각 행을 차례대로 계산
for i in range(1, n):
    left = [NEG_INF] * m
    right = [NEG_INF] * m

    # 먼저 위 행에서 내려온 값을 더함
    for j in range(m):
        dp[i][j] = dp[i - 1][j] + grid[i][j]

    # 왼쪽 → 오른쪽 순회
    left[0] = dp[i][0]
    for j in range(1, m):
        left[j] = max(left[j - 1] + grid[i][j], dp[i][j])

    # 오른쪽 → 왼쪽 순회
    right[m - 1] = dp[i][m - 1]
    for j in range(m - 2, -1, -1):
        right[j] = max(right[j + 1] + grid[i][j], dp[i][j])

    # 현재 행의 각 칸의 최댓값 갱신
    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[n - 1][m - 1])