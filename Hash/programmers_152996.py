def solution(weights):
    from collections import Counter
    counts = Counter(weights)
    answer = 0
    visited_pairs = set()
    ratios = [
        (1, 2),
        (2, 3),
        (3, 4),
        (1, 1),
        (4, 3),
        (3, 2),
        (2, 1),
    ]
    for w in counts:
        for numerator, denominator in ratios:
            if (w * numerator) % denominator == 0:
                target_weight = (w * numerator) // denominator
                if target_weight in counts:
                    pair = (min(w, target_weight), max(w, target_weight))
                    if pair not in visited_pairs:
                        if w == target_weight:
                            count = counts[w] * (counts[w] - 1) // 2
                            answer += count
                        else:
                            count = counts[w] * counts[target_weight]
                            answer += count
                        visited_pairs.add(pair)
    return answer