T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int,input().split())

    arr = [[] for _ in range(V + 1)]
    for i in range(E):
        S, G = map(int, input().split())
        arr[S].append(G)

    S1, G1 = map(int, input().split())
    flag = 0
    used = [0] * (V + 1)

    def dfs(now):
        global flag
        if now == G1:
            flag = 1
            return

        for i in arr[now]:
            if used[i] == 0:
                used[i] = 1
                dfs(i)
                used[i] = 0

    dfs(S1)

    print(f'#{test_case} {flag}')