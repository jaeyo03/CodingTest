import sys

# n : 접시수, d : 초밥 가짓수, k : 연속해서 먹는 접시수, c : 쿠폰 번호
n, d, k, c =  map(int, sys.stdin.readline().split())

sushi_line = []

for _ in range(n):
    sushi = sys.stdin.readline().strip()
    sushi_line.append(int(sushi))

answer = 0

for start in range(n) :
    selected_sushi = set()
    current = start
    count = 0

    while count < k :
        if current > n - 1 :
            current = current % n
        selected_sushi.add(sushi_line[current])
        current += 1
        count += 1

    selected_sushi.add(c)

    if len(selected_sushi) > answer :
        answer = len(selected_sushi)

print(answer)

# 추후 슬라이딩 윈도우 알고리즘으로 변경 필요