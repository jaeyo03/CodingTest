def solution(ingredient):
    answer = 0
    burger = [1,2,3,1]
    stack = []
    for i in ingredient:
        stack.append(i)
        # 마지막 4개씩 계속 체크
        if burger == stack[-4:]:
            answer += 1
            for _ in range(4):
                stack.pop()

    return answer