def solution(input_string):
    answer = ''
    answer_arr = []
    answer_dic = {}
    for i in range(len(input_string)):
        s = input_string[i]
        if s not in answer_dic.keys():
            answer_dic[s] = []

        answer_dic[s].append(i)

    for key in answer_dic.keys():
        arr = answer_dic[key]
        if len(arr) >= 2:
            for i in range(len(arr) - 1):
                if arr[i] + 1 != arr[i + 1]:
                    answer_arr.append(key)
                    break

    if answer_arr == []:
        answer_arr.append("N")

    answer_arr.sort()
    answer = "".join(answer_arr)
    return answer