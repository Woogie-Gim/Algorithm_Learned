T = int(input())
 
for test_case in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
 
    result = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
            if cnt > result:
                result = cnt
 
    print(f'#{test_case} {result}')