# delta 배열 / 방향 배열 / direct 배열

"""
[[3, 5, 4],
 [1, 1, 2],
 [1, 3, 9]]

입력 받은 좌표 기준으로 위 아래 좌 우의 합을 구한다고 가정

(1, 1) -> 5 + 3 + 1 + 2
(0, 0) -> 1 + 5

일단은 배열의 범위를 벗어났다고 생각하지 않고
"""

arr = [[3, 5, 4],
       [1, 1, 2],
       [1, 3, 9]]

# 1, 1 기준으로 위 아래 좌 우측에 있는 값들의 합을 구해서 출력하기

"""
1, 1 기준으로 y, x
위 : 0, 1    -1, 0
아래 : 2, 1   +1, 0
좌 : 1, 0     0, -1
우 : 1, 2     0, +1
"""

y, x = map(int, input().split())

directy = [-1, 1, 0, 0] # 위 아래 좌 우 움직임을 리스트화
directx = [0, 0, -1, 1]

Sum = 0
for i in range(4):
    dy = y + directy[i] # 임의의 좌표 dy에 상하좌우 움직임을 줌
    dx = x + directx[i]
    if dy < 0 or dx < 0 or dy > 2 or dx >2: #배열의 범위를 벗어날 경우
        continue
        # continue 밑에 코드가 실행되지 않고 반복문 맨 위로 올라감

    Sum += arr[dy][dx]

print(Sum) # 11

# 참고) 파이썬 스러운 코드

arr = [[3, 5, 4],
       [1, 1, 2],
       [1, 3, 9]]

y, x = map(int, input().split())

ans = 0

for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
    dy, dx = y + i, x + j
    if 0 <= dy < 3 and 0 <= dx < 3:
        ans += arr[dy][dx]

print(ans)

# 대각선의 곱 구하기

arr = [[3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8],
       [1, 2, 9, 1, 2],
       [3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8]]

y, x = map(int, input().split())

directy = [-1, -1, 1, 1]
directx = [-1, 1, -1, 1]

Gop = 1
for i in range(4):
    dy = y + directy[i]
    dx = x + directx[i]
    if dy < 0 or dx < 0 or dy > 4 or dx > 4:
        continue
    Gop *= arr[dy][dx]

print(Gop)

# n칸 만큼 떨어진 곳까지 합 구하기

arr = [[3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8],
       [1, 2, 9, 1, 2],
       [3, 5, 4, 5, 6],
       [1, 1, 2, 7, 8]]

y, x = map(int, input().split())

directy = [0, 0, -1, 1]
directx = [1, -1, 0, 0]

ans = 0

for i in range(4):
    for j in range(1, 4): # 몇 칸만큼 떨어진 곳까지 합을 구해야하기 때문에 2중 for문 사용
        dy = y + directy[i] * j
        dx = x + directx[i] * j
    if dy < 0 or dx < 0 or dy > 4 or dx > 4:
        continue
    ans += arr[dy][dx]

print(ans)

# 상하좌우의 값이 가장 큰 곳의 좌표 구하기

arr = [[1, 2, 3, 4],
       [1, 2, 9, 4],
       [1, 9, 3, 9],
       [1, 2, 9, 4]]

def isSum(y, x):
    directy = [0, 0, -1, 1]
    directx = [-1, 1, 0, 0]
    Sum = 0
    for i in range(4):
        dy = directy[i] + y
        dx = directx[i] + x
        if dy < 0 or dx < 0 or dy > 3 or dx > 3:
            continue
        return Sum
    
Max = -21e8
Max_i = 0
Max_j = 0
for i in range(4):
    for j in range(4):
        ret = isSum(i, j)
        if ret > Max:
            Max = ret
            Max_i = i
            Max_j = j

print(Max, Max_i, Max_j)

# 함수를 활용하여 시간복잡도 O(n ** 3) 에서 O(n ** 2)로 줄이기

# 대각선의 합 모두 구하기

arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

n = 4 # 4 * 4 배열
sum = [0] * (2 * n -1) # 대각 선 개수

for i in range(4):
    for j in range(4):
        sum[i + j] += arr[i][j]

print(*sum)