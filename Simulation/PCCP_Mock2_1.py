def solution(command):
    # 현재 방향 판단
    # 이동이라면 현재 방향에 맞게 이동
    # 방향 변경이면 현재 방향에 맞게 변경
    # 계속 진행
    answer = []
    current_direction = "up"
    x = 0
    y = 0
    moving = {"upG": [0, 1], "upB": [0, -1], "downG": [0, -1], "downB": [0, 1], "rightG": [1, 0], "rightB": [-1, 0],
              "leftG": [-1, 0], "leftB": [1, 0]}

    for c in command:
        if c == "G" or c == "B":
            temp = current_direction + c
            x += moving[temp][0]
            y += moving[temp][1]
        elif c == "R":
            if current_direction == "up":
                current_direction = "right"
            elif current_direction == "down":
                current_direction = "left"
            elif current_direction == "right":
                current_direction = "down"
            else:
                current_direction = "up"
        else:  # "L" 인 경우
            if current_direction == "up":
                current_direction = "left"
            elif current_direction == "down":
                current_direction = "right"
            elif current_direction == "right":
                current_direction = "up"
            else:
                current_direction = "down"

    answer.append(x)
    answer.append(y)
    return answer