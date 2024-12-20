def solution(order):
    answer = 0
    boxes = list(range(len(order), 0, -1))
    stack = []
    turn = 0

    while boxes:
        if stack:
            s = stack[-1]
            if order[turn] == s:
                stack.pop()
                answer += 1
                turn += 1
                continue

        box = boxes.pop()
        if order[turn] == box:
            answer += 1
            turn += 1
        else:
            stack.append(box)

    if stack:
        stack.reverse()
        if stack == order[turn:]:
            answer += len(stack)

    return answer