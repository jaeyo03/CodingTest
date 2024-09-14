from collections import deque
import heapq

def solution_answer(jobs):
    jobs.sort()
    n = len(jobs)
    time, total = 0, 0
    i = 0  # jobs의 인덱스
    heap = []

    while i < n or heap:
        # 현재 시간까지 도착한 모든 작업을 힙에 추가
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))  # (처리 시간, 요청 시간)
            i += 1

        if heap:
            proc_time, arrival = heapq.heappop(heap)
            time += proc_time
            total += time - arrival
        else:
            # 대기 중인 작업이 없으면 시간을 다음 작업의 요청 시간으로 점프
            time = jobs[i][0]

    return total // n

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