T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    Max1 = -21e8
    Max2 = -21e8
    Max3 = -21e8

    for i in range(100):
        Sum = 0
        for j in range(100):
            Sum += arr[i][j]
            if Sum > Max1:
                Max1 = Sum

    for a in range(100):
        Sum1 = 0
        for b in range(100):
            Sum1 += arr[b][a]
            if Sum1 > Max2:
                Max2 = Sum1

    for i in range(100):
        Sum2 = 0
        Sum3 = 0
        Sum2 += arr[i][i]
        Sum3 += arr[i][99 - i]
        if max(Sum2, Sum3) > Max3:
            Max3 = max(Sum2, Sum3)

    print(f'#{test_case} {max(Max1, Max2, Max3)}')