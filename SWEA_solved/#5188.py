dirct = [(0, 1), (1, 0)]
def dfs(x, y, s):
    global Min

    if s >= Min:
        return

    if x == N-1 and y == N-1:
        if s < Min:
            Min = s
        return

    for dx, dy in dirct:
        nx, ny = x + dx, y + dy

        if nx > -1 and nx < N and ny > -1 and ny < N:
            dfs(nx, ny, s + arr[nx][ny])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 21e8
    dfs(0, 0, arr[0][0])
    print(f'#{test_case} {Min}')