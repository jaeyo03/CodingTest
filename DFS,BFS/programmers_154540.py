def solution(maps):
    answer = []
    places = [[0] * len(maps[0]) for _ in range(len(maps))]

    dc = [1, -1, 0, 0]
    dr = [0, 0, -1, 1]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "X":
                continue
            else:
                if places[i][j] == 1:
                    continue
                else:
                    count = 0
                    stack = [(i, j)]
                    while stack:
                        r, c = stack.pop()
                        if places[r][c] == 0:
                            places[r][c] = 1
                            count += int(maps[r][c])
                            for inx in range(4):
                                new_r = r + dr[inx]
                                new_c = c + dc[inx]
                                if new_r < 0 or new_r >= len(maps) or new_c < 0 or new_c >= len(maps[0]) or maps[new_r][
                                    new_c] == "X" or places[new_r][new_c] == 1:
                                    continue
                                else:
                                    stack.append((new_r, new_c))
                    answer.append(count)

    answer.sort()

    if len(answer) == 0:
        answer = [-1]

    return answer