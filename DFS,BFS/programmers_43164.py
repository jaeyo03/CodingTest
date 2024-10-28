def solution(tickets):
    from collections import defaultdict

    graph = defaultdict(list)
    # 그래프 생성 및 정렬
    for a, b in tickets:
        graph[a].append(b)
    for key in graph.keys():
        graph[key].sort(reverse=True)

    route = []
    stack = ['ICN']

    while stack:
        top = stack[-1]
        # 연결된 티켓이 없거나 티켓을 모두 사용한 경우
        if not graph[top]:
            route.append(stack.pop())
        else:
            # 다음 공항으로 이동
            stack.append(graph[top].pop())
    # 경로를 뒤집어서 반환
    return route[::-1]

# 아래는 내가 작성한 틀린 풀이
def my_solution(tickets):
    answer = []
    start = "ICN"
    stack = [start]

    while stack:
        temp = []
        s = stack.pop()
        answer.append(s)
        for t in tickets:
            from_place = t[0]
            to_place = t[1]
            if s == from_place:
                temp.append(to_place)

        if temp:
            temp.sort(reverse=True)
            to = temp.pop()
            tickets.remove([s, to])  # 방문해서 쓴 티켓은 이제 끝
            stack.append(to)

    return answer