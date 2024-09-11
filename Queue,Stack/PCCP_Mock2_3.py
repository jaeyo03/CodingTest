from collections import deque


def solution(menu, order, k):
    answer = 0
    complete = -1  # 주원이가 음료 제작을 끝내는 시간
    queue = deque([])

    for t in range(k * (len(order) - 1) + 1):
        if t == complete:  # 완료했다면
            queue.popleft()
            complete = -1

        if t % k == 0:  # 손님이 들어오는 시각이라면
            inx = t // k
            queue.append(order[inx])

        if complete == -1 and queue:  # 주원이가 작업을 끝내고 기다리는 사람이 있다면 / 기다리는 사람이 없으면 주원이는 놀고 있으면 됨
            complete = t + menu[queue[0]]

        answer = max(answer, len(queue))

    return answer

# 아래는 내가 작성한 틀린 풀이

# def solution(menu, order, k):
#     answer = 0

#     end_time = 0 # 이게 곧 다음사람의 시작 시간
#     end_times = []

#     for i in range(len(order)):
#         end_time += menu[order[i]]
#         end_times.append(end_time)

#     total_time = end_times[-1]

#     new_end_times = {}

#     for e in end_times:
#         new_end_times[e] = 0

#     people = deque([0] * len(order))
#     waiting = deque([])


#     for i in range(k*(len(order)-1)+1):
#         if people and i%k == 0: #손님이 들어오는 시간이라면
#             p = people.popleft()
#             waiting.append(p)

#         if i in new_end_times.keys(): # 음료가 나온 손님이 있다면
#             waiting.popleft()

#         if len(waiting) > answer: # 최대값 갱신
#             answer = len(waiting)

#     return answer