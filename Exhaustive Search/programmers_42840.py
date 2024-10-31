def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_count, two_count, three_count = (0, 0, 0)

    for i in range(len(answers)):
        a = i % len(one)
        b = i % len(two)
        c = i % len(three)

        if one[a] == answers[i]:
            one_count += 1

        if two[b] == answers[i]:
            two_count += 1

        if three[c] == answers[i]:
            three_count += 1

    arr = [one_count, two_count, three_count]
    max_score = max(one_count, two_count, three_count)

    for i in range(len(arr)):
        if max_score == arr[i]:
            answer.append(i + 1)

    return answer