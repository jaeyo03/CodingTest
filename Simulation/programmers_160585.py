def solution(board):
    O_count = 0
    X_count = 0

    # O와 X의 개수를 센다
    for row in board:
        O_count += row.count('O')
        X_count += row.count('X')

    # O가 선공이므로 O의 수는 X의 수와 같거나 하나 많아야 한다
    if not (O_count == X_count or O_count == X_count + 1):
        return 0

    def check_winner(player):
        # 가로 확인
        for i in range(3):
            if all([cell == player for cell in board[i]]):
                return True
        # 세로 확인
        for i in range(3):
            if all([board[j][i] == player for j in range(3)]):
                return True
        # 대각선 확인
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    O_win = check_winner('O')
    X_win = check_winner('X')

    # 둘 다 승리할 수는 없다
    if O_win and X_win:
        return 0

    # O가 이겼다면 O의 수는 X보다 하나 많아야 한다
    if O_win and O_count != X_count + 1:
        return 0

    # X가 이겼다면 O와 X의 수가 같아야 한다
    if X_win and O_count != X_count:
        return 0

    return 1