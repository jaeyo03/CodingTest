# 3번
from collections import deque
from itertools import product
def solution(a,b,x):
    answer = [0]
    remains = [deque([x]),deque([]),deque([]),deque([]),deque([])]

    for i in range(1,5):
        remain = remains[i-1]
        next_remain = remains[i]
        count = 0
        while remain:
            health = remain.popleft()
            first_attack_okay = []

            for first_attack in range(a,b+1):
                if first_attack*2 >= health:
                    first_attack_okay.append(first_attack)
                    count += 1

            possible = product(range(a,b+1),repeat=2)
            for p in possible:
                first = p[0]
                second = p[1]
                # 이미 첫번째로 만족했다면 넘겨
                if first in first_attack_okay:
                    continue
                else:
                    whole_attack = first*2 + second
                    if whole_attack >= health:
                        count += 1
                    else:
                        next_remain.append(health-whole_attack)

        answer.append(count)
    return answer