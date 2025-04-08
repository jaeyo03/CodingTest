def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        consecutive = 0
        possible = True
        for stone in stones:
            if stone < mid:
                consecutive += 1
                if consecutive >= k:
                    possible = False
                    break
            else:
                consecutive = 0
        if possible:
            answer = mid  # mid 명이 건널 수 있음
            left = mid + 1
        else:
            right = mid - 1
    return answer

# 원래 내 풀이
# 원래는 0의 연속 갯수를 기록해서 해놓으려고 했는데 잘 되지는 않았음
def solution2(stones, k):
    answer = 0
    zero_marks = [False] * (len(stones) * 2 + 1)
    zero_chain_dict = {}  # 자신의 앞에 연속해서 몇개의 0이 있는지 기록하는 것

    inx = 0

    while True:
        is_jumped = False
        if stones[inx] > 0:
            stones[inx] -= 1
            if stones[inx] == 0:
                zero_marks[inx] = True
                zero_chain_dict[inx] = 1  # 자기 자신까지 갯수 포함
                if inx > 0:
                    if zero_marks[inx - 1]:
                        zero_chain_dict[inx - 1] += 1

                    if zero_marks[inx + 1]:
                        zero_chain_dict[inx] += zero_chain_dict[inx + 1]
        elif stones[inx] == 0:
            if zero_chain_dict[inx] < k:
                is_jumped = True
                inx += zero_chain_dict[inx]
            else:
                return answer

        if not is_jumped:
            inx += 1

        if inx >= len(stones):
            answer += 1
        inx %= len(stones)