# 정렬

# Sort

# 정렬 관련된 알고리즘

# 선택 정렬 selection sort
# 삽입 정렬 insert sort
# 버블 정렬 bubble sort

# 3가지 정렬 모두 시간 복잡도 O(n ** 2)
# 장점 : 쉽다, 단점 : 느리다

# counting sort - O(n)

arr = [4, 7, 1, 3, 5, 2]

# 1. 선택 정렬

"""
선택 정렬로 오름차순 정렬

4 <- 기준점 y / 비교대상 x
비교대상이 기준점보다 작을 경우 스왑

1 7 4 3 5 2 첫번째 정렬

1 4 7 3 5 2
1 3 7 4 5 2
1 2 7 4 5 3 두번째 정렬

1 2 4 7 5 3
1 2 3 7 5 4 세번째 정렬

1 2 3 5 7 4
1 2 3 4 7 5 네번째 정렬

1 2 3 4 5 7
"""

# 기준점은 0번 인덱스 부터 리스트 길이보다 1 작은 수

for y in range(len(arr) - 1):
    for x in range(y + 1, len(arr)):
        if arr[y] > arr[x]:
            arr[y], arr[x] = arr[x], arr[y]

print(arr) # [1, 2, 3, 4, 5, 7]

# 2. 삽입 정렬 insert sort
# 장점 : 쉽다, 단점 : 느리다
# 특징 : 이미 정렬된 데이터에서 새로 추가된 데이터를 정렬하기 좋음

# 삽입 정렬로 오름차순 정리

arr = [4, 7, 1, 3, 5]
# 새로운 배열에 하나씩 내려서 내릴 때 마다 비교해서 스왑해줌

result = [0] * 5

for i in range(5):
    result[i] = arr[i]
    for j in range(i, -1, -1):
        if result[j - 1] > result[j]:
            result[j - 1], result[j] = result[j], result[j - 1]
        else:
            break

print(result) # [1, 3, 4, 5, 7]

# 버블 정렬 Bubble sort
# 앞에서 부터 뒤를 비교하면서 계속해서 스왑

a = [8, 3, 12, 10, 1]

for i in range(len(a)-1, 0, -1): # 4 3 2 1
    for j in range(0, i): # i가 4일 때 j = 0, 1, 2, 3 # i가 3일 때 0, 1, 2....
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a) # [1, 3, 8, 10, 12]


# DAT
# Direct Address Table

# 보통 다중 for 문을 사용해서 element의 존재 여부나 개수를 샐 때 시간 복잡도는 O(n ** 2)
# DAT를 사용한다면 O(n)

# 빠른 검색을 위해서 사용하는 자료 구조

# DAT : 배열의 값을 다른 배열의 index로 활용하는

# bucket 이라는 리스트에 전부 0값으로 초기화
# 찾는 '정수'에 맞는 인덱스 위치에 1씩 증가시켜 개수를 찾는다
# bucket의 값은 a 배열에 해당 인덱스가 몇개씩 존재하는지 적혀있음

n = int(input()) # 길이가 n인
b = list(map(int, input().split())) #무작위 리스트를 받는다고 했을 때

bucket = [0] * 10
# bucket 등록

for i in range(len(b)):
    bucket[b[i]] += 1
    # index = a[i]
    # bucket[index] += 1
# n번 탐색

for i in range(len(b)):
    print(f'{b[i]}:{bucket[b[i]]}개')
# m번 탐색

# O(n + m) => O(n)의 속도

"""
DAT를 이용해서 문자열 입력받아 어떤 알파벳이 몇개 사용이 되었는지 출력 해보기
apple / a : 1개, p : 2개, l : 1개, e : 1개
몇 종류의 알파벳을 사용했는가? 4종류

문자열 -> 리스트화
['a', 'p', 'p', 'l', 'e']
소문자 a의 아스키코드값을 이용
200개 짜리 bucket을 만들어 index 활용하면 메모리를 너무 많이 사용

a : 97 -> a - a 0번 인덱스 / 26칸 짜리 버켓 배열만 필요
"""

lst = list(input())
bucket = [0] * 26

for i in range(len(lst)):
    index = ord(lst[i]) - ord('a')
    bucket[index] += 1

cnt = 0
for i in range(26):
    if bucket[i] > 0:
        cnt += 1 # 몇 종류의 알파벳이 사용되었는가

print(cnt) # 4

for i in range(26):
    if bucket[i] > 0:
        alpha = chr(i + ord('a'))
        print(f'{alpha}가 {bucket[i]}개 사용됨')

# 계수 정렬 Counting Sort

"""
4 7 1 4 2 4 3
counting sort
계수 정렬
O(n)
1. DAT bucket 등록
2. 누적합 구하기
3. 값 넣기

10 칸짜리 bucket 만들기

bucket = [0] * 10

각 수에 해당하는 인덱스에 해당하는 곳에 1씩 증가

증가된 값의 누적 합 구하기
0: 0 / 1: 1 / 2: 1 / 3: 1 / 4: 3 / 5: 0 / 6: 0 / 7: 1 / 8: 0 / 9: 0
0 1 2 3 6 6 6 7 7 7

값 넣기
-1 씩 해서 맞는 인덱스에 다시 넣어주기

4의 누적합은 6 / 3개가 있으니 5 -> 4 -> 3

O(3n) -> O(n)

누적합이 의미하는 것은 해당 인덱스보다 작은 게 앞에 몇개 있는지 표시가 됨

그 값보다 앞에 몇개가 있는지 알기 때문에 -1한 값이 자연스럽게 인덱스가 됨

counting sort 끝
"""

n = int(input())
a = list(map(int, input().split()))

bucket = [0] * 11
# 버켓 등록 / 정해진 길이는 없지만 넉넉하게 만들어 둠

# 누적합 구하기
for i in range(1, len(bucket)):
    bucket[i] += bucket[i - 1]

# 값 넣기
result = [0] * n
for i in range(n):
    bucket[a[i]] -= 1
    index = bucket[a[i]]
    result[index] = a[i]

# 출력하기
print(*result)

"""
DAT 라는 자료구조는 빠른 검색을 위한 자료구조
100개 짜리 리스트에서 30개 짜리 리스트 값들이 존재하는지 볼 때
2중 for문을 사용하면 3000번 탐색

bucket 리스트를 사용하면 130번 탐색

단, 상황에 맞게 사용을 해야 한다

[1, 2, 8, 9, 110000000]

5개의 리스트를 탐색하기 위해서 110000001 의 길이를 가진 bucket을 만드는 것은 비효율적

DAT의 한계:
['Bob', 'Kate', 'Kevin', 'Amy']
처럼 문자열로 이루어진 리스트에선 사용하기 어렵다

이럴 땐 hash와 BST를 활용하여 극복 가능
"""