from collections import deque

def solution(s):
    # 집합에서 이게 어디서 나온 튜플인지 찾는 문제
    # 튜플의 원소에는 순서가 정해져 있다. 종류가 같아도 배열이 다르면 다른 튜플
    numbers = []
    answer = []
    s = s.split("},{")
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]

    for num in s:
        num = num.split(",")
        numbers.append(num)

    # numbers에 숫자들 모았음
    numbers.sort(key=lambda x: len(x))

    arr = deque(numbers)

    before = []
    while arr:
        a = arr.popleft()
        if len(a) == 1:
            before = a
            answer.append(int(a[0]))
        else:
            for i in a:
                if i not in before:
                    answer.append(int(i))
                    before = a

    return answer