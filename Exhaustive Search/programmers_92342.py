from itertools import combinations

def solution(n, info):
    answer = []
    max_point = 0

    for i in range(1, 12):
        for combi in combinations(list(range(11)), i):  # 하나의 조합
            total_arrows = n
            result = [0] * 11
            success = True
            for i in combi:
                need_arrows = info[i] + 1
                if need_arrows > total_arrows:
                    success = False
                    break
                else:
                    total_arrows -= need_arrows
                    result[i] = need_arrows

            # 화살 다 안 썼으면 , 남은 화살은 0 점에 버리기
            if total_arrows > 0:
                result[10] = total_arrows

            # 화살도 다 쓰고 가능한 경우라면
            if success:
                lion = 0
                peach = 0
                # 점수 계산
                for i in range(11):
                    if result[i] > info[i]:
                        lion += 10 - i
                    elif info[i] >= result[i] and info[i] != 0:
                        peach += 10 - i
                if lion > peach and (lion - peach) >= max_point:
                    max_point = lion - peach
                    answer.append((result, lion - peach))
            else:
                continue

    # answer.sort(key = lambda x : (x[1],x[0][10],x[0][9],x[0][8],x[0][7],x[0][6],x[0][5],x[0][4],x[0][3],x[0][2],x[0][1],x[0][0]),reverse=True)
    answer.sort(key=lambda x: (x[1], x[0][::-1]), reverse=True)

    if len(answer) == 0:
        answer = [-1]
    else:
        answer = answer[0][0]

    return answer