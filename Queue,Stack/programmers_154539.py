def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        num = numbers[i]

        while stack and stack[-1][1] < num:  # 전에 있는 숫자들 중 num보다 작은 것들만 넣기
            inx, _ = stack.pop()
            answer[inx] = num

        stack.append((i, num))

    return answer