def solution(video_len, pos, op_start, op_end, commands):
    # 모든거 초로 바꿔버려
    def to_sec(time):
        h, s = time.split(":")
        h = int(h) * 60
        s = int(s)
        total = h + s
        return total

    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    opening = list(range(op_start, op_end + 1))
    # 현재 위치 오프닝이면 오프닝 끝나는 구간으로 이동

    if pos in opening:
        pos = op_end

    for c in commands:
        if c == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        elif c == "next":
            if video_len - pos < 10:
                pos = video_len
            else:
                pos += 10

        if pos in opening:
            pos = op_end

    hour = str(pos // 60)
    minute = str(pos % 60)

    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute

    return hour + ":" + minute