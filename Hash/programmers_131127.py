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