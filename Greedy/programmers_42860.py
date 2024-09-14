import string

def solution(name):
    answer = 0
    upper_arr = list(string.ascii_uppercase)
    target = []
    # A에서 바뀌어야 하는 부분 체크
    for idx in range(len(name)):
        if name[idx] != "A":
            target.append(idx)

    def find_min(start, target):
        will_move = 0
        MIN = 9999
        for t in target:
            if t == 0:
                MIN = 0
                will_move = 0
                break
            else:
                d = min(abs(start - t), abs(start - (t - len(name))))
                if d < MIN:
                    MIN = d
                    will_move = t

        return will_move, MIN

    start = 0  # 맨 처음부터 시작
    while target:
        will_move, d = find_min(start, target)
        answer += d
        start = will_move
        alpha_start = upper_arr.index(name[will_move])
        d2 = min(alpha_start, abs(alpha_start - len(upper_arr)))
        answer += d2
        target.remove(will_move)

    return answer