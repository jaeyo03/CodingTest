import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    num_string = sys.stdin.readline().strip()
    num_string = num_string.split('.')
    for i in range(len(num_string)) :
        num_string[i] = int(num_string[i])
    if len(num_string) == 1:
        num_string.append(-1)
    data.append(num_string)

data.sort(key=lambda x: (x[0],x[1]))

for d in data:
    if d[1] == -1:
        print(d[0])
    else :
        print(str(d[0]) + '.' + str(d[1]))