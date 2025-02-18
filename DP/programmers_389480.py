def solution(info, n, m):
    # (a, b): A와 B가 지금까지 남긴 흔적
    possible = {(0, 0)}

    for a_cost, b_cost in info:
        new_possible = set()
        for a, b in possible:
            # A가 물건을 훔치는 경우
            if a + a_cost < n:
                new_possible.add((a + a_cost, b))
            # B가 물건을 훔치는 경우
            if b + b_cost < m:
                new_possible.add((a, b + b_cost))
        possible = new_possible
        # 만약 이번 단계에서 가능한 상태가 하나도 없다면 (어떠한 선택도 불가능하다면)
        if not possible:
            return -1

    # 가능한 최종 상태 중 A 흔적 합의 최소 반환
    return min(a for a, b in possible)