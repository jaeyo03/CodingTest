def solution(enroll, referral, seller, amount):
    answer = []
    graph = dict()
    graph['center'] = ['center', 0]

    for i in range(len(enroll)):
        if referral[i] == '-':
            graph[enroll[i]] = ['center', 0]
        else:
            graph[enroll[i]] = [referral[i], 0]

    for i in range(len(seller)):
        sell = seller[i]
        money = amount[i] * 100

        give = money // 10
        graph[sell][1] += money - give

        stack = [[graph[sell][0], give]]
        while stack:
            next_sell, money = stack.pop()
            if money < 1:
                continue

            give = money // 10
            if next_sell == 'center':
                graph[next_sell][1] += give
            else:
                graph[next_sell][1] += money - give
                stack.append([graph[next_sell][0], give])

    for e in enroll:
        answer.append(graph[e][1])
    return answer