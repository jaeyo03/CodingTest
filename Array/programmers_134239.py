def solution(k, ranges):
    answer = []
    numbers = [k]
    spaces = []
    # make numbers
    while k > 1:
        if k % 2 == 0:
            k = k/2
        else :
            k = k*3 + 1
        numbers.append(k)
    
    for i in range(len(numbers)-1):
        s = (numbers[i] + numbers[i+1]) / 2
        spaces.append(s)
    
    for r in ranges:
        start = r[0]
        end = len(numbers) - 1 + r[1]
        total = 0
        if start == end:
            answer.append(0)
            continue
        
        if end < start:
            answer.append(-1)
            continue
        
        for i in range(start,end):
            total += spaces[i]
        
        answer.append(total)
                
    return answer
