T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    lst = []
    Min, Max = 0, N - 1

    while Min <= Max:
        lst.append(arr[Max])
        Max -= 1

        lst.append(arr[Min])
        Min += 1

    result = ' '.join(map(str, lst[:10]))

    print(f'#{test_case} {result}')
