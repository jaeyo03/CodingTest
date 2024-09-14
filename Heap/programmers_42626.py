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

def solution_2(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 1:
            s = heapq.heappop(scoville)
            if s >= K:
                break
            else:
                answer = -1
                break
        else:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)

            if s1 >= K:
                break
            else:
                new = s1 + 2 * s2
                heapq.heappush(scoville, new)
                answer += 1

    return answer