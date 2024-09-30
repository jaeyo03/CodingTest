def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for s in skill_trees:
        s = list(s)
        stack = []
        i = 0
        for string in s:
            if string in skill:
                stack.append(string)
                i += 1

        if stack[0:i] == skill[0:i]:
            answer += 1

    return answer