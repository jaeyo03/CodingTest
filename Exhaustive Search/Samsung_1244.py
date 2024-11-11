# Read the number of test cases
T = int(input())

for test_case in range(1, T + 1):
    input_line = input().split()
    num_str = input_line[0]
    k = int(input_line[1])
    num_list = list(num_str)
    n = len(num_list)
    visited = dict()
    max_value = [0]  # Use a list to allow modification within dfs

    def dfs(cnt):
        state = (''.join(num_list), cnt)
        if visited.get(state, False):
            return
        visited[state] = True
        if cnt == k:
            max_value[0] = max(max_value[0], int(''.join(num_list)))
            return
        for i in range(n):
            for j in range(i + 1, n):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                dfs(cnt + 1)
                num_list[i], num_list[j] = num_list[j], num_list[i]

    dfs(0)
    print(f"#{test_case} {max_value[0]}")