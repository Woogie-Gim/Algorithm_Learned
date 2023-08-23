T = int(input())
 
for test_case in range(1, T + 1):
    arr = list(map(int, input()))
 
    handclap = 0
    employee = 0
 
    for i in range(1, len(arr)):
        handclap += arr[i - 1]
        if arr[i] == 0:
            continue
        if i > handclap:
            employee += i - handclap
            handclap += i - handclap
 
 
    print(f'#{test_case} {employee}')