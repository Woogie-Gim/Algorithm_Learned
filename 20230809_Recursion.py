# 재귀 Recursion
# 함수 자기 자신을 계속 호출하는 함수
# 예시 주사위 던지기

"""
for i in range(1, 7):
    for j in range(1, 7):
        print(i, j)

주사위 개수가 늘어날 수록 시간복잡도는 느려진다.

3중 4중 ...
주사위 개수를 입력받는다고 하면 for문의 개수를 설정하기엔 어렵다
"""

# 주사위 n개를 던져서 나오는 경우의 수를 재귀함수로 표현

n = int(input())

path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return
    
    for i in range(6):
        path[level] = i + 1
        abc(level + 1)
        # 자기 자신을 호출하는 함수


abc(0)

"""
main -> abc()
abc() -> abc()
abc() -> abc() ....

코드가 끝나지 않고 무한 반복

따라서 가장 먼저 해야할 일은 무한 호출을 막아야 한다

abc(0) 호출 -> abc(0) -> abc(1) -> return
return -> abc(1) / return은 함수가 호출된 곳으로
"""   

# 1 3 5 7 7 5 3 1
# 재귀 실습해보기
# 디버깅과 손버깅으로 따라가면서 이해하기

def abc(level):
    print(level)
    if level == 7:
        print(level)
        return
    abc(level + 2)
    print(level)

abc(1)

def abc(level):
    if level == 2:
        return
    abc(level + 1)
    abc(level + 1)

abc(0)


def abc(level):
    if level == 2:
        return

    for i in range(2):
        abc(level + 1)

abc(0)

# 12
def abc(level):
    if level == 2:
        return
    for i in range(2):
        print('#', end = '')
        abc(level + 1)
        print('#', end = '')

abc(0)

# 13
def abc(level):
    print('#', end='')
    if level == 2:
        return
    for i in range(2):
        abc(level + 1)
        print('#', end = '')

abc(0)

# 7
def abc(level):

    if level == 2:
        print('#', end='')
        return

    print('#', end='')
    for i in range(2):
        abc(level + 1)

abc(0)

# 110
def abc(level):

    if level == 2:
        return

    for i in range(2):
        abc(level + 1)

    print(level, end='')

abc(0)

def abc(level):
    print('#', end='')
    if level == 2:
        print('#', end='')
        return
    print('#', end='')

    for i in range(2):
        print('#', end='')
        abc(level + 1)
        print('#', end='')
    print('#', end='')

abc(0)

# 누적합
# 재귀로 구현하기


# 방법 1) sum을 매개변수로 놓고 누적합 출력하기
def abc(level, sum):
    print(sum, end = ' ')
    if level == 5:
        return
    abc(level + 1, sum + arr[level + 1])
    # abc(level + 1, sum += arr[level + 1]) -> 3이 7로 바뀐 다음에 함수에 들어감 3출력 불가


arr = [3, 4, 5, 1, 6, 9]
      #0  1  2  3  4  5

abc(0, arr[0]) # level sum

# 방법 2) sum 전역변수

sum = arr[0]
def abc(level):
    global sum
    print(sum, end = ' ') # 들어가면서 누적합 출력
    if level == 5:
        return
    sum += arr[level + 1]
    abc(level + 1)


abc(0) # level


# 누적합 거꾸로 출력하기
# 방법 1)

def abc(level, sum):
    if level == 5:
        print(sum, end=' ')
        return
    abc(level + 1, sum + arr[level + 1])
    print(sum, end = ' ')


arr = [3, 4, 5, 1, 6, 9]
      #0  1  2  3  4  5

abc(0, arr[0]) # level sum


# 방법 2)

arr = [3, 4, 5, 1, 6, 9]
sum = arr[0]
def abc(level):
    global sum
    if level == 5:
        print(sum, end = ' ')
        return
    sum += arr[level + 1] # sum 값이 함수에 들어갈 때 더해진 채로 들어감 level1 일 때 7로 들어감
    abc(level + 1)
    sum -= arr[level + 1]
    print(sum, end = ' ')


abc(0) # level


# 3 7 1 2로 이루어진 무작위 카드 뭉치 3개에서 각 묶음 에서 한장씩 뽑았을 때 합이 10장이 되는 경우의 수

#                             O
#                         3  7  1  2
#                      3712 3712 3712 3712
#                            ....


# Sum 을 매개변수로 놓았을 때
cnt = 0
def abc(level, Sum):
    global cnt
    if level == 3:
        if Sum == 10:
            cnt += 1
        return

    for i in range(4):
        abc(level + 1, Sum + (card[i]))


card = [3, 7, 1, 2]
abc(0, 0) # level, Sum
print(cnt)

# Sum을 전역변수로 놓았을 때

arr = [3, 7, 1, 2]
cnt = 0
Sum = 0

def abc(level):
    global cnt, Sum

    if level == 3:
        if Sum == 10:
            cnt += 1
        return

    for i in range(4):
        Sum += arr[i]
        abc(level + 1)
        Sum -= arr[i]

abc(0) #level
print(cnt)

# 3, 4, 1, 7, 6 숫자가 섞여 있는 n개의 카드 묶음에서 카드를
# 각각 1장씩 뽑아서 더했을 때 합이 10 이하로 나오는 경우는 몇가지 일까요?

# branch 는 배열의 개수 / level 이 n

arr = [3, 4, 1, 7, 6]
cnt = 0
n = int(input())

def abc(level, Sum):
    global cnt, n
    if Sum > 10:
        return
    if level == n:
        if Sum <= 10:
            cnt += 1
        return

    for i in range(5):
        abc(level + 1, Sum + arr[i])

abc(0, 0)
print(cnt)


"""
재귀 함수가 다녀간 경로 출력하기

A B C D
로 섞인 카드 뭉치 3개에서 무작위로 카드를 뽑는다

AAA
AAB
AAC
.
.
.
DDD

path 배열마다 재귀 경로를 지나갈 때마다 추가
"""

arr = ['A', 'B', 'C', 'D']
path = [''] * 3

def abc(level):
    if level == 3:
        for i in range(level):
            print(path[i], end = ' ')
        print()
        return
    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)

abc(0)

# n개의 주사위를 던졌을 때 나올 수 있는 모든 경우의 수

# level = n / branch = 6
# 경로 출력

n = int(input())
path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return
    for i in range(6):
        path[level] = i + 1
        abc(level + 1)

abc(0)

n = int(input())
arr = [1, 2, 3, 4]
path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(4):
        path[level] = arr[i]
        abc(level + 1)


abc(0)

# 순열
"""
한 번 뽑았던 카드는 중복해서 뽑지 않는 경우
뽑았던 카드인지 체크 하면서 재귀를 나아감
used or visited 배열 만들어줌

used Index
0 1 2 3
A B C D

A 를 지났을 때 0번 인덱스에 1 체크를 하고 진행
지나갈 때마다 1 체크
return 될 때 체크 된 곳을 0 으로 다시 바꿔줌
"""


# 중복순열 => 그냥 모든 경우의 수를 다 출력 !!! (주사위 던지기)

# 순열 => 올림픽 금, 은, 동
n = int(input())
card = ['A', 'B', 'C', 'D']
path = [0] * n
used = [0] * len(card)

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(4):
        if used[i] == 1: # 체크 되어 있는 곳을 들어가는 것을 막음
            continue
        path[level] = card[i]
        used[i] = 1
        abc(level + 1)
        used[i] = 0 # 돌아올 때 다시 체크 되어 있는 곳을 0으로 바꿔줌

abc(0)


# 조합 (nCm)

"""
              main
           A              B                C              D
    A    B   C   D  A   B   C   D   A   B    C   D   A  B   C    D
ABCD ABCD ABCDABCD ABCDABCDABCDABCD ABCDABCDABCDABCD ABCDABCDABCDABCD
 
나올 수 있는 조합
ABC
.
.
.
BCD (A에 들어갈 필요가 없음)

그 전에 들어왔던 가지 +1 하면서 탐색
"""

# 중복 순열로 셋팅을 해놓고 코드를 어떻게 추가하면 되는지
# 조합 => 농구팀을 예로 들었음

# 첫번째 방법 : 전 브랜치에서 체크된 level - 1 번 인덱스와 앞으로 들어갈 것을 비교
n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(4):
        if level > 0 and path[level - 1] >= card[i]:
            continue
        # 전 브랜치보다 +1 을 탐색해서 나가기 때문에 level - 1 번 인덱스 보다 card[i]가 작으면 탐색할 필요가 없다
        path[level] = card[i]
        abc(level + 1)


abc(0)

# 값이 오름차순이 아닌 경우
# 반복문을 돌릴 때 다음 브랜치로 가서 인덱스도 전 인덱스 다음부터 탐색하면 가능

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(start, 4):
        path[level] = card[i]
        abc(level + 1, i + 1)


abc(0, 0)

# 중복 조합 (112 == 121)
"""
1, 2, 3, 4로 중복 조합 만들기

111
112
113
114
122
123
124
133
134
144
222
.
.
.

들어갔던 가지 '에서' 부터 다시 시작
"""

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(start, 4):
        path[level] = card[i]
        abc(level + 1, i)


abc(0, 0)

# 중복 순열을 출력하는데 특정 문자로 시작하는 문자는 전부 제외

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level == 1 and path[level - 1] == 'B': # 진입 후 리턴 하는 코드
        return
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(4):
        # if level == 0 and card[i] == 'B': # 아예 진입을 하지 않는 경우
        #     continue
        path[level] = card[i]

        abc(level + 1, i)

abc(0, 0)


# 중복 순열 / 연속해서 같은 카드 뽑지 않는 경우 모두 출력

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level > 1 and path[level - 1] == path[level - 2]: # 2번 방법 진입 후 리턴하는 경우
        return # 일단 진입을 했기 때문에 전 배열과 전전배열이 같으면 리턴
    if level == n:
        for i in range(n):
            print(path[i], end = ' ')
        print()
        return

    for i in range(4):
        path[level] = card[i]
        # if level > 0 and path[level - 1] == card[i]: # 1번 방법 진입을 안하는 경우
        #     continue
        abc(level + 1, i)

abc(0, 0)


# 중복 순열 / 뽑았을 때 'C'는 제외 하고 출력

n = 3
path = [''] * n
card = ['A', 'B', 'C', 'D']

def abc(level, start):
    if level > 0 and path[level - 1] == 'C': # 진입 후 리턴 하는 경우
        return
    if level == n:
        for i in range(n):
            print(path[i], end = '')
        print()
        return

    for i in range(4):
        # if card[i] == 'C': # 진입을 안하는 경우
        #     continue
        path[level] = card[i]
        abc(level + 1, i)

abc(0, 0)