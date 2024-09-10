import heapq

def solution(ability, number):
    # 최소 힙으로 변환
    heapq.heapify(ability)

    for _ in range(number):
        # 가장 작은 두 값을 추출
        one = heapq.heappop(ability)
        two = heapq.heappop(ability)

        # 합 계산
        total = one + two

        # 합한 값을 다시 힙에 삽입
        heapq.heappush(ability, total)
        heapq.heappush(ability, total)

        # heappop, heappush 기억하자!
    return sum(ability)