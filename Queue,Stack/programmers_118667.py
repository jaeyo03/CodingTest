from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    q1s = sum(queue1)
    q2s = sum(queue2)
    total = q1s + q2s

    # 두 큐의 합이 홀수인 경우
    if total % 2 == 1:
        return -1

    target = total // 2
    count = 0

    # queue1이 더 큰 경우와 queue2가 더 큰 경우를 나눠서 처리
    if q1s > q2s:
        source, dest, source_sum, dest_sum = queue1, queue2, q1s, q2s
    else:
        source, dest, source_sum, dest_sum = queue2, queue1, q2s, q1s

    while source_sum != target:
        tmp = source.popleft()
        dest.append(tmp)

        source_sum -= tmp
        dest_sum += tmp

        count += 1

        # 일반적인 경우에는 큰 큐의 원소를 작은 큐로 하나씩 전환
        # 큰 큐의 원소가 작은 큐의 합보다 큰 경우에는 작은 큐의 모든 원소를 큰 큐로 전환
        if source_sum < dest_sum:
            while source:
                tmp = source.popleft()
                dest.append(tmp)
                source_sum -= tmp
                dest_sum += tmp
                count += 1

    return count