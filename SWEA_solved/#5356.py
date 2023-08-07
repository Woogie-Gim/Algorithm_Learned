T = int(input())

for test_case in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]

    result = ''

    max_len = max(len(row) for row in arr)

    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                result += arr[j][i]

    print(f'#{test_case} {result}')