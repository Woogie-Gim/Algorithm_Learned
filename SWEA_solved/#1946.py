T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [(list(map(str, input().split()))) for i in range(N)]

    result = ''
    for i in range(N):
        result += arr[i][0] * int(arr[i][1])

    print(f'#{test_case}')
    for i in range(0, len(result), 10):
        print(result[i:i + 10])