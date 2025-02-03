import sys
n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int,sys.stdin.readline().split())))
attacks = []
for _ in range(2) :
    attacks.append(tuple(map(int,sys.stdin.readline().split())))

for attack in attacks :
    start,end = attack

    for inx in range(start-1,end) :
        row = graph[inx]
        for i in range(len(row)):
            if row[i] == 1:
                row[i] = 0
                break
answer = 0
for g in graph :
    answer += g.count(1)

print(answer)