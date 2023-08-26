T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    sheep = 1
    ans = []
    while 1:
        K = N
        K *= sheep
        for i in str(K):
            arr.append(i)
 
        arr.sort()
        ans = list(set(arr))
        sheep += 1
 
        result = 0
        for i in range(10):
            if str(i) in ans:
                result += 1
 
        if result == 10:
            print(f'#{test_case} {K}')
            break