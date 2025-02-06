import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(tuple(map(int, sys.stdin.readline().strip().split())))

answer = 0
current = 0
for d in data:
    p, f = d
    diff = abs(current - p)
    if diff <= f:
        current += 1

print(current)