T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for y in range(len(arr) - 1):
        for x in range(y + 1, len(arr)):
            if arr[y] > arr[x]:
                arr[y], arr[x] = arr[x], arr[y]

    result = ' '.join(map(str, arr))

    flag = 0
    for i in arr:
        print(f'#{test_case} {result}')
        flag = 1
        break


# 선택 정렬을 활용한 오름차순 정렬