def solution(data, col, row_begin, row_end):
    answer = 0
    # 마이너스를 활용하는거 기억하기!!
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    S_i = []

    for inx, d in enumerate(data):
        total = 0
        for num in d:
            total += num % (inx + 1)
        S_i.append(total)

    for i in range(row_begin - 1, row_end):
        if i == row_begin - 1:
            answer = S_i[row_begin - 1]
        else:
            # python 에서 bitwise 는 ^ 이다.
            answer = answer ^ S_i[i]

    return answer