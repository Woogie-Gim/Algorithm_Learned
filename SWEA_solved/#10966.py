from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    visited = [[21e8] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append([i, j, 1])
                visited[i][j] = 0

    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
                continue
            if arr[ny][nx] == 'L':
                if visited[ny][nx] > visited[y][x] + d:
                    visited[ny][nx] = d
                    q.append([ny, nx, d + 1])
    ans = 0
    for i in visited:
        ans += sum(i)

    print(f'#{test_case} {ans}')


for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    bfs()