def solution(number, k):
    collected = []

    for i, num in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break

        collected.append(num)

    # 번호가 큰 수 부터 차례대로 정렬 되어 있는 예외 상황
    if len(collected) == len(number):
        collected = collected[:-k]

    return "".join(collected)