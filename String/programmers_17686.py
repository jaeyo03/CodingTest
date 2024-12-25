def get_head_and_num(file):
    for i in range(len(file)):
        if file[i].isnumeric():  # 숫자면
            for j in range(i, len(file)):
                if not file[j].isnumeric():
                    return file[:i], file[i:j]
                if j == len(file) - 1:
                    # 문자열 끝이 숫자인 예외 경우도 생각하기
                    return file[:i], file[i:j + 1]

def solution(files):
    answer = []
    arr = []
    for originalIndex, file in enumerate(files):
        head, number = get_head_and_num(file)
        arr.append((originalIndex, head.lower(), int(number), file)) # index, head, number, 원래 파일 이름
        # lower 는 모든 문자를 소문자로 바꿔준다
        # int() 는 강력하다. "000" -> 0 , "0010" -> 10 이런식으로 다 숫자로 잘 바꿔줌.

    arr.sort(key=lambda x: (x[1], x[2], x[0]))

    for a in arr:
        answer.append(a[3])

    return answer