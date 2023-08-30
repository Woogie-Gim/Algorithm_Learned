def dfs(level):
    global ans
    if level == N - 1:
        a = []
        for i in path:
            if i != 0:
                a.append(i)
        a.insert(0, 1)
        a.append(1)
        ans.append(a)
        return

    for i in range(N - 1):
        if visited[i] == 0:
            visited[i] = 1
            path[level] = lst[i]
            dfs(level + 1)
            visited[i] = 0



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for i in range(2, N + 1):
        lst.append(i)
    visited = [0] * (N - 1)
    ans = []
    path = [0] * (N - 1)
    dfs(0)
    Min = 21e8
    for i in ans:
        Sum = 0
        for j in range(N):
            Sum += arr[i[j] - 1][i[j + 1] - 1]
        if Sum < Min:
            Min = Sum

    print(f'#{test_case} {Min}')