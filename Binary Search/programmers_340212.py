import sys

def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = sys.maxsize  # 큰 값 얻는 법
    while start < end:
        level = int((end + start) / 2)
        t = times[0]
        for i in range(1, len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i - 1]

            if diff <= level:
                t += time_cur
            elif diff > level:
                wrong = diff - level
                t += wrong * time_cur
                t += wrong * time_prev
                t += time_cur

        if limit < t:
            start = level + 1  # 시간이 더 오래 걸리면 난이도를 높여야 함
        else:
            end = level

    answer = start

    return answer