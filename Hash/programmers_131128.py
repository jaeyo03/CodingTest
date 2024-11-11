def solution(X, Y):
    x_numbers = dict()
    answer_arr = []
    for x in X:
        if x not in x_numbers.keys():
            x_numbers[x] = 1
        else:
            x_numbers[x] += 1

    for y in Y:
        if y in x_numbers.keys():
            if x_numbers[y] > 0:
                x_numbers[y] -= 1
                answer_arr.append(y)

    answer_arr.sort(reverse=True)
    answer = "".join(answer_arr)

    if answer == "":
        answer = "-1"

    if set(answer) == set(['0']):
        answer = "0"

    return answer