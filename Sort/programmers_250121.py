def solution(data, ext, val_ext, sort_by):
    target = []

    i = 0
    if ext == "code":
        i = 0
    elif ext == "date":
        i = 1
    elif ext == "maximum":
        i = 2
    else:
        i = 3

    # 뽑기
    for d in data:
        if d[i] < val_ext:
            target.append(d)

    k = 0
    if sort_by == "code":
        k = 0
    elif sort_by == "date":
        k = 1
    elif sort_by == "maximum":
        k = 2
    else:
        k = 3

    target.sort(key=lambda x: x[k])

    return target