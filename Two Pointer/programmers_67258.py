from collections import defaultdict

def solution(gems):
    num_types = len(set(gems))
    gem_counter = defaultdict(int)
    answer = [0, len(gems)]
    start = 0
    end = 0
    min_length = len(gems) + 1
    while end < len(gems):
        gem_counter[gems[end]] += 1
        end += 1
        # Check if current window contains all types
        while len(gem_counter) == num_types:
            if end - start < min_length:
                min_length = end - start
                answer = [start +1 , end]  # converting to 1-based index
            gem_counter[gems[start]] -= 1
            if gem_counter[gems[start]] == 0:
                del gem_counter[gems[start]]
            start += 1
    return answer
