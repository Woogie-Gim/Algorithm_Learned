T = int(input())
 
for test_case in range(1, T + 1):
    strr = input()
    s = []
 
    for i in strr:
        if not s or s[-1] != i:
            s.append(i)
        else:
            s.pop()
 
    print(f'#{test_case} {len(s)}')