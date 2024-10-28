from collections import deque

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