import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif not scoville:
            answer = -1
            break
        else:
            min2 = heapq.heappop(scoville)
            new = min1 + 2 * min2
            heapq.heappush(scoville, new)
            answer += 1

    return answer