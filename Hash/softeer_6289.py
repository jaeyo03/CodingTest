import sys
N,M = map(int,sys.stdin.readline().split(' '))
W = list(map(int,sys.stdin.readline().split(' ')))

ok = [True] * N

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split(' '))
    A = a - 1
    B = b - 1
    if W[A] > W[B] :
        ok[B] = False
    elif W[A] < W[B] :
        ok[A] = False
    else :
        ok[A] = False
        ok[B] = False

print(ok.count(True))