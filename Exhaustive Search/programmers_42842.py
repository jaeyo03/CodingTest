def solution(brown, yellow):
    answer = []

    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = int(yellow / h)
            if w < h:
                break
            else:
                if brown == 2 * w + 2 * h + 4:
                    answer = [w + 2, h + 2]
    return answer