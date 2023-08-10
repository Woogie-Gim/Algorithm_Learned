T = int(input())

for test_case in range(1, T + 1):
    def check_bracket(strr):
        brackets = {")": "(", "}": "{", "]": "["}
        s = []
        for i in strr:
            if i in brackets.values():
                s.append(i)
            elif i in brackets:
                if not s or s.pop() != brackets[i]:
                    return 0
        return 1 if not s else 0

    strr = input()
    print(f'#{test_case} {check_bracket(strr)}')