
import sys
import heapq

input = sys.stdin.readline

n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

INF = 10**9
# dp[node][free_used] = 해당 상태에 도달할 때 현재까지의 '최대 지불 케이블 비용'의 최솟값
dp = [[INF] * (k + 1) for _ in range(n + 1)]
dp[1][0] = 0

# 우선순위 큐에 (현재 최대 비용, 현재 노드, 지금까지 사용한 무료 케이블 수)를 저장
pq = []
heapq.heappush(pq, (0, 1, 0))

while pq:
    cur_cost, node, used_free = heapq.heappop(pq)
    if dp[node][used_free] != cur_cost:
        continue
    # 목적지에 도달하면 현재까지의 최대 비용이 답
    if node == n:
        print(cur_cost)
        sys.exit(0)
    for nxt, cost in graph[node]:
        # 옵션 1: 해당 케이블을 유료로 사용
        new_cost = max(cur_cost, cost)
        if new_cost < dp[nxt][used_free]:
            dp[nxt][used_free] = new_cost
            heapq.heappush(pq, (new_cost, nxt, used_free))
        # 옵션 2: 무료 사용 기회가 남아있다면, 비용 부담 없이 케이블 연결
        if used_free < k and cur_cost < dp[nxt][used_free + 1]:
            dp[nxt][used_free + 1] = cur_cost
            heapq.heappush(pq, (cur_cost, nxt, used_free + 1))

print(-1)


# 틀린 내 풀이

import sys
from collections import deque
from copy import deepcopy
import heapq

n, p, k = map(int, sys.stdin.readline().strip().split())
graph = dict()
answer = 9999999

for _ in range(p) :
    start, end, price = map(int, sys.stdin.readline().strip().split())
    if graph.get(start) :
        graph[start].append((end, price))
    else:
        graph[start] = [(end, price)]

    if graph.get(end) :
        graph[end].append((start, price))
    else:
        graph[end] = [(start, price)]

visited = [False] * (n + 1)
visited[1] = True
q = deque([(1,[],visited)])

def find_price(heap) :
    print(heap)
    count = 0
    while count < k :
        heapq.heappop(heap)
        count += 1

    max_price = heapq.heappop(heap)
    return max_price

while q :
    v, prices, visited = q.popleft()
    if v == n :
        total_price = find_price(prices)
        if total_price < answer :
            answer = total_price
        break

    for next_v in graph[v] :
        new_prices = deepcopy(prices)
        new_visited = deepcopy(visited)
        if not visited[next_v[0]] :
            new_visited[next_v[0]] = True
            heapq.heappush(new_prices, -next_v[1])
            q.append((next_v[0], new_prices, new_visited))

print(-answer)