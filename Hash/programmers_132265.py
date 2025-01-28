from collections import deque
def solution(topping):
    answer = 0
    A = dict()
    B = dict()
    
    for t in topping:
        try:
            B[t] += 1
        except KeyError:
            B[t] = 1
    
    B_deque = deque(topping)
    
    while len(B_deque) > 0 :
        b = B_deque.popleft()
        if B[b] > 1 :
            B[b] -= 1
            A[b] = 1
        elif B[b] == 1:
            B.pop(b) # pop으로 키를 없앨 수 있다
            A[b] = 1
            
        if len(A.keys()) == len(B.keys()) :
            answer += 1
        
    return answer
