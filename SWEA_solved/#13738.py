T = int(input())

for test_case in range(1, T + 1):
    def isfind(str1, str2):
        for i in range(len(str2)):
            alpha = ''.join(map(str, str2[i: (i + len(str1))]))
            if alpha == str1:
                return 1

        return 0

    str1 = str(input())
    str2 = list(map(str, input()))

    result = isfind(str1, str2)

    print(f'#{test_case} {result}')