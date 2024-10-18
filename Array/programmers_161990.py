def solution(wallpaper):
    answer = []
    x = len(wallpaper[0])
    y = len(wallpaper)
    tmp = set()
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                tmp.add((i, j))
                tmp.add((i + 1, j + 1))
    tmp = list(tmp)

    max_x = 0
    min_x = 999
    max_y = 0
    min_y = 999

    for point in tmp:
        y = point[0]
        x = point[1]
        if y < min_y:
            min_y = y

        if y > max_y:
            max_y = y

        if x < min_x:
            min_x = x

        if x > max_x:
            max_x = x

    return [min_y, min_x, max_y, max_x]