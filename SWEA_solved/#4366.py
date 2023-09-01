T = int(input())

for test_case in range(1, T + 1):
    a = input()
    b = list(map(int, input()))

    n = len(a)
    m = len(b)
    ans = 0

    binary = int(a, 2)
    bin_lst = [0] * n
    for i in range(n):
        bin_lst[i] = binary ^ (1 << i)

    for i in range(m):
        num1 = 0
        num2 = 0
        for j in range(m):
            if i != j:
                num1 = num1 * 3 + b[j]
                num2 = num2 * 3 + b[j]
            else:
                num1 = num1 * 3 + (b[j] + 1) % 3
                num2 = num2 * 3 + (b[j] + 2) % 3

        if num1 in bin_lst:
            ans = num1
            break
        if num2 in bin_lst:
            ans = num2
            break

    print(f'#{test_case} {ans}')
