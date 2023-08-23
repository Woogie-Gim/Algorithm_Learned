def WBR(level, prev_color_idx):
    if level == N - 2:
        if not 'B' in path:
            return
        for i in range(len(path)):
            ans.append(''.join(path))
        return
 
    for i in range(3):
        if i >= prev_color_idx:
            path[level] = color[i]
            WBR(level + 1, i)
 
 
T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
 
    cnt = 0
    for i in range(M):
        if arr[0][i] != 'W':
            cnt += 1
 
    for j in range(M):
        if arr[N - 1][j] != 'R':
            cnt += 1
 
    color = ['W', 'B', 'R']
    path = [0] * (N - 2)
    ans = []
    WBR(0, 0)
    result = list(set(ans))
    Min = 21e8
    paint = cnt
 
 
    for a in range(len(result)):
        cnt = paint
        for b in range(1, N - 1):
            for k in range(M):
                if arr[b][k] != result[a][b - 1]:
                    cnt += 1
        if Min > cnt:
            Min = cnt
 
    print(f'#{test_case} {Min}')