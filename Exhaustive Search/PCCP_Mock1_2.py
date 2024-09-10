from itertools import permutations

def solution(ability):
    answer = 0
    permu = list(permutations(list(range(len(ability))), len(ability[0])))

    for p in permu:
        value = 0
        for i in range(len(p)):
            value += ability[p[i]][i]
        if answer < value:
            answer = value

    return answer