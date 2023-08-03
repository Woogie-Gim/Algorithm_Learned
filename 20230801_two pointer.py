# 투포인터

# 1. 특정 조건을 만족하는 연속 부분 수열을 찾는다.
# 2. 특정 조건을 만족하는 두 개의 수를 찾는다.


# 1 5 8 7 3

# 1 8
# 1 7
# 1 8 7
# 부분수열 (연속된 것만 부분 수열이라고 하는 경우가 있음)

# 1 7 8 은 부분수열이 아니다 순서를 바꾸지 않으면 나올 수 없기 때문에

# 연속 부분 수열 => 투 포인터, prefix sum + binary search
# 1 5
# 1 5 8
# 5 8 7

# 백준 2003번
# 수들의 합 2
# 연속 부분 수열의 합이 M 인 경우의 수

# 10 5
# 1 2 3 4 2 5 3 1 1 2
# 2 3 / 5 / 3 1 1

# 시작이 1인 연속 수열의 합은 개수가 많아질 수록 증가할 수 밖에 없다

# 1 2 3 4 2 5 3 1 1 2
# s
# e
# 1

# s
#   e
# 6
# 안된다는 걸 알았을 때
# 시작점은 다음 위치로 가고 끝점은 앞으로 올 필요가 없다
# 어떤 구간의 합이 5보다 작았기 때문에 끝점이 앞으로 간 것이기 때문에 앞으로 올 필요가 없다
# 합이 5를 잧은 상황에선 시작점 끝점 중 어떤 것이 뒤로 가도 상관 없다

# O(n)


# n, m = map(int, input().split())
#
# arr = list(map(int, input().split())) + [0]
# arr.sort()
# s = 0
# e = 0
# total = arr[0]
#
# cnt = 0
# while e < n:
#     if total == m:
#         cnt += 1
#         e += 1
#         total += arr[e]
#     elif total < m:
#         e += 1
#         total += arr[e]
#     else:
#         total -= arr[s]
#         s += 1

# print(cnt)

# 예외 경우를 없애기 위해 앞이나 뒤에 요소를 넣어 주는 것을 패딩

# 2. 특정 조건을 만족하는 두 개의 수를 찾는다.

# 백준 3273번

# 서로 다른 양의 정수로 이루어진 수열 에서 합이 입력 값이 되는 쌍의 개수를 구한다

# 9
# 5 12 7 10 9 1 2 3 11
# 13

# 정렬해서 생각

# 1 2 3 5 7 9 10 11 12
# s                  e
# 13

# 찾았다면 둘 중 어느것이 움직여도 더 찾을 방법은 없다
# 둘의 합이 13보다 작다면 이미 큰 수들을 사용했기 때문에 s가 한칸 뒤로
# 13보다 크다면 e가 뒤로 가면 된다
# 서로 다른 양의 정수 이므로 e가 s보다 큰 경우의 수

# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())
#
# s = 0
# e = n -1
# cnt = 0
#
# while s < e:
#     if arr[s] + arr[e] == x:
#         cnt += 1
#         s += 1
#     elif arr[s] +arr[e] < x:
#         s += 1
#     else:
#         e -= 1
#
# print(cnt)

# 투포인터의 기본 틀

# 1. 특정 조건을 만족하는 연속 부분 수열을 찾는다.
#   s = 0, e = 0 출발
#   종료조건 : e < n
#   같이 뒤로 간다

# 2. 특정 조건을 만족하는 두 개의 수를 찾는다
#   s = 0, e = 0 출발
#   반복조건 : s < e
#   서로에게 다가간다.

# 2309번 일곱난쟁이

# 합이 100이 되는 일곱개의 수를 출력하는 문제
# 합이 (총합 -100) 되는 2개의 수를 찾는 문제가 됨

arr = [int(input()) for i in range(9)]
total = sum(arr)

arr.sort()

s = 0
e = 8
while s < e:
    if arr[s] + arr[e] == total - 100:
        for i in range(9):
            if i == s or i == e:
                continue
            print(arr[i])

        break
    elif arr[s] + arr[e] < total - 100:
        s += 1
    else:
        e -= 1

# 항상 리스트는 정렬

# 백준 2467번 용액
# 두 개의 수의 합이 0에 제일 가까운 수를 찾아라
# 이중 for 문 못씀

# -99 -2 -1 4 98
# s           e

# -99 98
# -99 입장에선 98 보단 더 커야 0보다 가까워진다
# 합이 음수일 경우 s가 뒤로
# 합이 양수일 경우 e가 앞으로

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = 0
e = n - 1
x = arr[0]
y = arr[n - 1]

while s < e:
    if abs(x + y) > abs(arr[s] + arr[e]):
        x = arr[s]
        y = arr[e]

    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(x, y)

# 백준 9007번 카누 선수 문제

# 300 4
# 60 52 80 40
# 75 68 88 63
# 48 93 48 54
# 56 73 49 75

# 135 128 148 123 127 ...
# 104 121 ....

# 123 127 128 135 148
# s
# 104 121
#     e

# 두 수의 합이 크다면 s가 뒤로 가고
# 두 수의 합이 작다면 e가 앞으로 가고
# 잘알려진 쉽게 풀려진 문제를 웰논

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(4)]

    a = []
    b = []

    for i in range(n):
        for j in range(n):
            a.append(arr[0][i] + arr[1][j])
            b.append(arr[2][i] + arr[3][j])

    a.sort()
    b.sort()

    s = 0
    e = len(b) - 1
    ans = a[s] + b[e]
    while s < len(a) and e > 0:
        if abs(ans - m) > abs(a[s] + b[e] -m):
            ans = a[s] + b[e]

        if a[s] + b[e] > m:
            e -= 1
        else:
            s += 1

    print(ans)

# 백준 22988번 재활용 캠페인

# 1. 이미 가득찬 것들 제외
# 2. 투포인터로 두개씩 묶어서 제작
# 3. 남은 것들 // 3이 추가

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
s = 0
e = n -1
for i in range(n)[::-1]:
    if arr[i] == m:
        cnt += 1
        e = i -1
        x -= 1

while s < e:
    if 2 * (arr[s] + arr[e]) >= m:
        cnt += 1
        x -= 2
        s += 1
        e -= 1
    else:
        s += 1

print(cnt + x // 3)
