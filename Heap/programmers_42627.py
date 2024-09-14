from collections import deque
import heapq


def solution(jobs):
    answer = 0
    count = len(jobs)
    jobs.sort(key=lambda x: x[0])

    for j in jobs:
        temp = j[0]
        j[0] = j[1]
        j[1] = temp

    jobs = deque(jobs)

    complete = -1  # 디스크의 현재 작업 여부
    waiting_queue = []  # 작업 중일때 들어오는 작업이 기다리는 힙큐
    heapq.heapify(waiting_queue)
    end = []  # 작업 끝난 애들 넣는 스택

    t = 0
    while len(end) < count:
        if t == complete:  # 작업이 끝났다면
            end.append(0)
            complete = -1

        if len(jobs) > 0 and t == jobs[0][1]:
            if complete == -1 and len(waiting_queue) == 0:  # 작업 안하고 기다리는 애가 없으면
                job = jobs.popleft()
                complete = t + job[0]
                answer += complete - job[1]
            elif complete == -1 and len(waiting_queue) > 0:  # 작업 안하고 기다리는 애 존재
                job = jobs.popleft()
                p = heapq.heappushpop(waiting_queue, job)
                complete = t + p[0]
                answer += complete - p[1]
            elif complete != -1:
                job = jobs.popleft()
                heapq.heappush(waiting_queue, job)
        else:
            if complete == -1 and len(waiting_queue) > 0:
                p = heapq.heappop(waiting_queue)
                complete = t + p[0]
                answer += complete - p[1]

        t += 1

    return int(answer / count)