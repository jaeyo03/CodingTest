from copy import deepcopy

def solution(want, number, discount):
    answer = 0
    want_dict = dict()

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(0, len(discount) - 9):
        temp_dict = deepcopy(want_dict)
        discounts = discount[i:i + 10]

        for d in discounts:
            if d in temp_dict.keys():
                if temp_dict[d] > 0:
                    temp_dict[d] -= 1

        all_discounted = True

        for key in temp_dict.keys():
            if temp_dict[key] > 0:
                all_discounted = False
                break

        if all_discounted:
            answer += 1

    return answer

# 아래 풀이가 더 deepcopy를 안 써서 더 빠른 풀이
def better_solution(want, number, discount):
    answer = 0
    want_indexes = dict()

    for i in range(len(want)):
        want_indexes[want[i]] = i

    for i in range(0, len(discount) - 9):
        discounts = discount[i:i + 10]
        count_arr = [0] * len(want)

        for d in discounts:
            if d in want:
                inx = want_indexes[d]
                if count_arr[inx] < number[inx]:
                    count_arr[inx] += 1

        if count_arr == number:
            answer += 1

    return answer