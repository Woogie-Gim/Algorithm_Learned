T = 10
 
for test_case in range(1, T + 1):
    length, pwd = map(str, input().split())
    s = []
 
    for i in pwd:
        if not s or s[-1] != i:
            s.append(i)
        else:
            s.pop()
 
    ans = ''.join(s)
    print(f'#{test_case} {ans}')