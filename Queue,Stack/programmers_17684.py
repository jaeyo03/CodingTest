import string
from collections import deque

def solution(msg):
    answer = []
    records = dict()
    record_inx = 27
    for inx,word in enumerate(list(string.ascii_uppercase)) :
        records[word] = inx + 1

    w = msg[0]
    msg_q = deque(list(msg[1:]))

    while msg_q :
        c = msg_q.popleft()
        if (records.get(w+c)) : # 사전에 있다면
            w = w + c
        else : # 사전에 없다면
            records[w+c] = record_inx
            record_inx += 1
            answer.append(records[w]) # 언제 answer 에 넣을지 잘 생각하기!
            w = c

    answer.append(records[w])
    return answer