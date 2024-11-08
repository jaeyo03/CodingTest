# 2번
from copy import deepcopy
from collections import deque

def solution(arr, brr):
    arr = deque(arr)
    brr = deque(brr)
    queue = deque([(arr, brr, 0)])

    while queue:
        temp_arr, temp_brr, count = queue.popleft()
        is_same = False

        for i in range(len(temp_arr)):
            if temp_arr[i] == 1 and temp_brr[i] == 1:
                is_same = True
                break

        if not is_same:
            return count

        # 1
        a1 = deepcopy(temp_arr)
        b1 = deepcopy(temp_brr)
        a1.appendleft(0)
        b1.append(0)
        queue.append((a1, b1, count + 2))

        # 2
        a2 = deepcopy(temp_arr)
        b2 = deepcopy(temp_brr)
        a2.append(0)
        b2.appendleft(0)
        queue.append((a2, b2, count + 2))

arr = [1,0,1,1,0,0]
brr = [0,1,1,1,0,1]
print(solution(arr, brr))