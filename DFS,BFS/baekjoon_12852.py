n = int(input())

def solution(n):
    from collections import deque
    from copy import deepcopy
    visited = [0] * (10 ** 6 + 1)
    visited[n] = 1
    queue = deque([(n, 0, [n])])

    while queue:
        num, count, record = queue.popleft()

        if num == 1:
            return (count, record)

        if num % 3 == 0:
            tmp1 = int(num/3)
            if visited[tmp1] == 0:
                visited[tmp1] = 1
                arr1 = deepcopy(record)
                arr1.append(tmp1)
                queue.append((tmp1, count+1, arr1))

        if num % 2 == 0:
            tmp2 = int(num/2)
            if visited[tmp2] == 0:
                visited[tmp2] = 1
                arr2 = deepcopy(record)
                arr2.append(tmp2)
                queue.append((tmp2, count+1, arr2))

        if num >= 2:
            tmp3 = num - 1
            if visited[tmp3] == 0:
                visited[tmp3] = 1
                arr3 = deepcopy(record)
                arr3.append(tmp3)
                queue.append((tmp3, count+1, arr3))

count_ans, record_ans = solution(n)
print(count_ans)
print(" ".join(map(str, record_ans)))