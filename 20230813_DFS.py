# 자료 구조
# 선형 자료구조 : 스택 큐 덱 / 데이터 끼리의 관계는 생각 안하고 들어간 순서를 중요시
# 관계형 자료구조 : 그래프 트리 / 정보간의 관계를 중요시 함
# 점들을 노드 혹은 정점이라고 부름 / 관계는 엣지 혹은 간선이라고 부름
# 주로 노드 / 간선이라고 부름

# 그래프는 노드들끼리 연결이 되어 있다 안되어 있다가 중요한게 아님
# 노드는 필수요소지만 간선은 필수요소가 아님
# 직간접적으로 연결되어 있는 것들을 연결 요소 라고 부를 거임
# 단일 노드만 있어도 연결 요소 1개로 측정
# 연결 요소의 크기는 노드의 개수를 의미함

# DFS, BFS 모두 되는 문제는 보통 연결 요소 문제
# DFS 문제 => 경로 정보, 이전으로 들어간다, 이제까지 왔던 길에 이것들이 몇개 있냐
# BFS 문제 => 최단 거리

# 양방향 연결이 되어 있을 경우 방문 처리를 함으로써 cycle을 방지한다
# 방문처리가 되었더라도 함수가 끝이 나면 함수가 호출 됐던 곳으로 return
# 같은 연결 요소에 있는 노드는 방문 처리를 할 수 있다 -> dfs를 다 돌리면 전부 방문 처리가 된다
# 시작노드 s 끝 노드 e
# s에서 e를 갈 수 있나? -> s에서 dfs 를 전부 돌리고 e가 방문처리 되어 있는지 확인한다
# s가 포함된 연결요소의 크기 구하기 -> s에서 dfs 돌린 후 방문처리된 노드의 수 구하기
# 연결 요소의 개수 -> 방문 안한 노드를 볼 때마다 카운트 하기

# 인접 리스트로 DFS 표현하기
"""
[
0 : [],
1 : [],
2 : [],
3 : [],
4 : []
5 : []
6 : []
7 : []
8 : []
]
갈 수 있는 곳을 리스트 안에 표현
"""
# 백준 2606번 바이러스

# 방문 처리 개수 세는 방식
n = int(input()) #노드 번호
m = int(input()) #간선 번호

v = [[] for i in range(n + 1)] # n번 노드가 필요하기 때문에 n + 1개의 range

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a) # 양방향이기 때문에 b에 a를 append

# DFS 일반적인 코드

visited = [False for i in range(n + 1)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

dfs(1)

cnt = 0
for i in range(n + 1):
    if visited[i]:
        cnt += 1

print(cnt - 1)
# 다른 방법으로는 어떤 코드가 몇번 실행됐는지 궁금하다면 코드랑 딱 붙여서 사용하면 더 간단한 코드 가능

# return 하는 방식 함수를 실행하고 몇개의 노드를 방문했는지 리턴하고 싶다
n = int(input())
m = int(input())

v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]

def dfs(cur):
    cnt = 1 # 나 한개 있다
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        cnt += dfs(nxt)

    return cnt

print(dfs(1) - 1) # 이 문제는 자기 자신을 빼야 하니까


# 백준 11724 연결 요소의 개수

n, m = map(int, input().split())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)

# 백준 16562 친구비

# 1(10) <-> 3(20) / 4(20) <-> 2(10), 4(20) <-> 5(30)
# 각 연결 요소에서 가장 작은 값을 가진 노드를 찾고 모두 더해줌

n, m, k = map(int, input().split())

arr = [0] + list(map(int, input().split()))
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]

def dfs(cur):
    ret = arr[cur] # 내가 얼마 인지
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        ret = min(ret, dfs(nxt))

    return ret

ans = 0
for i in range(1, n + 1):
    if visited[i]:
        continue

    ans += dfs(i)

if ans <= k:
    print(ans)
else:
    print('Oh no')


# 플러드 필 (flood fill)
# 지도에서 땅이랑 바다 구분
# 2차원 맵에서 같은 연결 요소들을 묶어 놓은 문제
# 노드 하나 => 정수 두개로 표현(좌표)

# 백준 2667 단지번호 붙이기

n = int(input())
arr = [input() for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n
def dfs(y, x):
    ret = 1
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not in_range(ny, nx) or visited[ny][nx] or arr[ny][nx] != '1':
            continue
        # 순서 중요 / 범위 체크 할 때 visited가 앞에 있으면 범위 벗어나서 runtime error 발생 가능
        ret += dfs(ny, nx)

    return ret

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or arr[i][j] == '0':
            continue

        cnt += 1
        ans.append(dfs(i, j))

ans.sort()

print(cnt)
for i in ans:
    print(i)