from itertools import combinations

def solution(n, tops):
    answer = 0
    possible = []
    for i in range(2 * n):
        possible.append([i, i + 1])

    for inx, top in enumerate(tops):
        if top == 1:
            possible.append([2 * inx + 1])

    for i in range(1, n + 1):
        temp = list(combinations(possible, i))
        for t in temp:
            count = 0
            values = set()
            for value in t:
                for v in value:
                    values.add(v)
                    count += 1
            if len(values) == count:
                answer += 1

    return (answer + 1) % 10007