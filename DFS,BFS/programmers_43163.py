from collections import deque

def is_baby(a, b):
    count = 0
    for i in range(len(a)): # 문제 조건을 잘 읽고 단어 길이를 입력 단어에 맞게 조정하기!
        if a[i] != b[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def my_solution(begin, target, words):
    visited = dict()
    for w in words:
        visited[w] = False

    queue = deque([(begin, 0)])
    visited[begin] = True

    while queue:
        word, count = queue.popleft()
        for next_w in words:
            if is_baby(word, next_w) and not visited[next_w]:
                if next_w == target:
                    return count + 1
                queue.append((next_w, count + 1))
                visited[next_w] = True

    return 0

# 아래는 지피티 풀이
def solution(begin, target, words):
    if target not in words:
        return 0

    visited = {word: False for word in words}
    queue = deque()
    queue.append((begin, 0))

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps

        for word in words:
            if not visited[word]:
                # 현재 단어와 비교하여 다른 알파벳 수 계산
                diff = sum([1 for a, b in zip(current_word, word) if a != b])
                if diff == 1:
                    visited[word] = True
                    queue.append((word, steps + 1))

    return 0