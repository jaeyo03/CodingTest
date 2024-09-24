def solution(targets):
    # 폭격 미사일의 끝 지점을 기준으로 정렬합니다.
    targets.sort(key=lambda x: x[1])
    answer = 0
    # 마지막 요격 미사일의 발사 지점을 저장합니다.
    point = -1e9  # 충분히 작은 값으로 초기화

    for s, e in targets:
        # 만약 현재 폭격 미사일이 이전 요격 미사일로 요격되지 않는다면
        if not (s < point < e):
            # 새로운 요격 미사일을 발사합니다.
            point = e - 0.5  # e보다 작은 임의의 실수
            answer += 1

    return answer