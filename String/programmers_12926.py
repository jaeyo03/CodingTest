import string

def solution(s, n):
    answer = ''
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)

    s = list(s)
    for word in s:
        if word == " ":
            answer += word
        elif word in lower:
            inx = lower.index(word)
            inx += n
            if inx >= len(lower):
                inx -= len(lower)
            word = lower[inx]
            answer += word
        elif word in upper:
            inx = upper.index(word)
            inx += n
            if inx >= len(upper):
                inx -= len(upper)
            word = upper[inx]
            answer += word

    return answer