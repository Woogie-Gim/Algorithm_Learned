T = int(input())


def isNum1(y, x):
    Sum1 = 0
    for i in range(y, y + 3): # 3 * 3 배열 검사
        for j in range(x, x + 3):
            Sum1 += arr[i][j]

    if Sum1 == 45: # 1 ~ 9 까지의 합 45
        return 1
    else:
        return 0


def isNum2(y, x):
    Sum2 = 0
    for k in range(9): # 세로 검사
        Sum2 += arr[k][x]

    if Sum2 == 45:
        return 1
    else:
        return 0


def isNum3(y, x):
    Sum3 = 0
    for l in range(9): # 가로 검사
        Sum3 += arr[y][l]

    if Sum3 == 45:
        return 1
    else:
        return 0

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for i in range(9)]

    for i in range(0, 9, 3):
        for j in range(0, 9, 3): # 3 * 3 배열의 가장 첫번째 좌표만 검사
            ret1 = isNum1(i, j)
            if ret1 == 0:
                break
        if ret1 == 0:
            break

    for k in range(9):
        for l in range(9):
            ret2 = isNum2(k, l)
            if ret2 == 0:
                break
        if ret2 == 0:
            break
    for a in range(9):
        for b in range(9):
            ret3 = isNum3(a, b)
            if ret3 == 0:
                break
        if ret3 == 0:
            break

    ans = 0
    if ret1 == 1 and ret2 == 1 and ret3 == 1:
        ans = 1

    print(f'#{test_case} {ans}')