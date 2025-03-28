import sys
n, k = map(int, sys.stdin.readline().strip().split())
# 0 흰색
# 1 빨간색
# 2 파란색

graph = []
player_graph = [[0] * n for _ in range(n)]
player_info = dict()

for _ in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(arr)

for i in range(k):
    row, col, direction = map(int, sys.stdin.readline().strip().split())
    player_graph[row - 1][col - 1] = [[i + 1, direction - 1]]
    player_info[i + 1] = [(row - 1,col - 1), direction - 1]

dy = [0,0,-1,1] # 0,1,2,3
dx = [1,-1,0,0]

turn = 0
answer = -1
def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

has_answer = False
while turn <= 1000 :
    if has_answer :
        break

    for key in range(1, k + 1) :
        y,x = player_info[key][0]
        direction = player_info[key][1]
        has_other = False
        only_change_direction = False

        if type(player_graph[y][x]) == list :
            if len(player_graph[y][x]) > 1 :
                if player_graph[y][x][0][0] != key :
                    continue
                else :
                    has_other = True

        # default는 흰색을 만나는거
        next_y = y + dy[direction]
        next_x = x + dx[direction]

        # 체스판을 벗어나는 경우
        if (next_y < 0 or next_y >= n or next_x < 0 or next_x >= n) or graph[next_y][next_x] == 2 :
            direction = change_direction(direction)
            next_y = y + dy[direction]
            next_x = x + dx[direction]
            if (next_y < 0 or next_y >= n or next_x < 0 or next_x >= n) or graph[next_y][next_x] == 2 :
                next_y = y
                next_x = x
                only_change_direction = True

        if only_change_direction :
            if has_other :
                player_graph[y][x][0] = [key, direction]
            else :
                player_graph[y][x] = [[key, direction]]
            continue

        # 빨간색이라면
        if graph[next_y][next_x] == 1:
            if has_other :
                player_graph[y][x].reverse()

        if has_other :
            for item in player_graph[y][x]:
                num = item[0]
                if num == key :
                    player_info[key][0] = (next_y, next_x)
                    player_info[num][1] = direction
                    if type(player_graph[next_y][next_x]) == list :
                        player_graph[next_y][next_x].append([key, direction])
                    else :
                        player_graph[next_y][next_x] = [[key, direction]]
                else :
                    player_info[num][0] = (next_y, next_x)
                    if type(player_graph[next_y][next_x]) == list :
                        player_graph[next_y][next_x].append(item)
                    else :
                        player_graph[next_y][next_x] = [item]
            player_graph[y][x] = 0
        else :
            player_info[key][0] = (next_y, next_x)
            player_info[key][1] = direction
            if type(player_graph[next_y][next_x]) == list:
                player_graph[next_y][next_x].append([key, direction])
            else:
                player_graph[next_y][next_x] = [[key, direction]]
            player_graph[y][x] = 0

    turn += 1

    for _y in range(len(player_graph)):
        for _x in range(len(player_graph[_y])):
            if type(player_graph[_y][_x]) == list:
                if len(player_graph[_y][_x]) >= 4:
                    answer = turn
                    has_answer = True
                    break

print(answer)