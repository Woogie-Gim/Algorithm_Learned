from collections import deque

pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
pipe_reverse = [1, 0, 3, 2]


def bfs(N, M):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited[sty][stx] = 1
    q = deque()
    q.append([sty, stx])

    while q:
        x, y = q.popleft()
        for d in pipe[arr[x][y]]:
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and pipe_reverse[d] in pipe[arr[nx][ny]]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


T = int(input())
for test_case in range(1, T + 1):
    n, m, sty, stx, ed = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    bfs(n, m)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= ed:
                cnt += 1

    print(f'#{test_case} {cnt}')