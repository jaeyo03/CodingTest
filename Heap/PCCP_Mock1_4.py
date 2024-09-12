import heapq
from collections import deque


def solution(program):
    answer = [0] * 11

    # 기다리는 줄을 힙큐로 설정하자, 기다리는 프로그램의 우선순위는 점수로 결정되니까
    waiting = []
    heapq.heapify(waiting)

    # 호출시각 별로 딕셔너리 생성
    start_times = {}
    for p in program:
        time = p[1]
        if time not in start_times.keys():
            start_times[time] = []

        start_times[time].append(p)

    # 프로그램 점수로 정렬
    for key in start_times.keys():
        start_times[key].sort(key=lambda x: x[0])
        start_times[key] = deque(start_times[key])

    complete_times = []
    complete = -1
    t = 0

    while len(complete_times) < len(program):
        if t == complete:
            complete = -1

        if t in start_times.keys():  # 들어오는 애가 있는 경우
            if complete == -1 and len(waiting) == 0:  # 하는 일이 없고 기다리는애가 없다면
                # 처음거 진행
                p = start_times[t].popleft()
                complete = t + p[2]
                complete_times.append(complete)
                answer[p[0]] += t - p[1]
                while len(start_times[t]) > 0:
                    p = start_times[t].popleft()
                    heapq.heappush(waiting, p)
            elif complete != -1:  # 하는일이 있다면
                while len(start_times[t]) > 0:
                    p = start_times[t].popleft()
                    heapq.heappush(waiting, p)
            elif complete == -1 and len(waiting) > 0:  # 하는 일이 없고 기다리는애가 있다면
                while len(start_times[t]) > 0:
                    p = start_times[t].popleft()
                    heapq.heappush(waiting, p)
                p = heapq.heappop(waiting)
                complete = t + p[2]
                complete_times.append(complete)
                answer[p[0]] += t - p[1]
        else:
            # 들어오는애는 없지만 기다리는 애들이 있는 경우
            if complete == -1 and len(waiting) > 0:
                p = heapq.heappop(waiting)
                complete = t + p[2]
                complete_times.append(complete)
                answer[p[0]] += t - p[1]

        t += 1

    answer[0] = complete_times[-1]

    return answer