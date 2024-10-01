import heapq

def solution(operations):
    queue = []
    heapq.heapify(queue)

    for o in operations:
        command, num = o.split(" ")
        num = int(num)

        if command == "I":
            heapq.heappush(queue, num)
        elif command == "D" and len(queue) > 0:
            if num == -1:
                heapq.heappop(queue)
            else:
                queue.remove(max(queue))

    if len(queue) == 0:
        answer = [0, 0]
    else:
        answer = [max(queue), queue[0]]

    return answer