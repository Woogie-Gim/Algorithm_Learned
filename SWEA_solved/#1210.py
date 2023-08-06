T = 10

for test_case in range(1, T + 1):
    N = int(input())
    ladder = list(list(map(int, input().split())) for i in range(100))

    s = ladder[99].index(2)
    x, y = 99, s
    arr = [[0] * 100 for _ in range(100)]
    while x != 0:
        arr[x][y] = 1
        if y - 1 >= 0 and ladder[x][y - 1] and arr[x][y - 1] == 0:
            y -= 1
            continue
        elif y + 1 < 100 and ladder[x][y + 1] and arr[x][y + 1] == 0:
            y += 1
            continue
        else:
            x -= 1

    ans = y

    print(f'#{test_case} {ans}')