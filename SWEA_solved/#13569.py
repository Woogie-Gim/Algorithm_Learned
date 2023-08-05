for test_case in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Max = 0

    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1

        if cnt > Max:
            Max = cnt


    print(f'#{test_case} {Max}')