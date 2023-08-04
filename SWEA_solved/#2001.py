T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
 
    def isMax(y, x):
 
        Sum = 0
        for i in range(y, y + M): # M * M 배열의 모든 합을 구하기
            for j in range(x, x + M):
                if i < 0 or j < 0 or i >= N or j >= N:
                    continue
                Sum += arr[i][j]
        return Sum
 
    Max = -21e8 
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ret = isMax(i, j)
            if ret > Max: # Max 값 구하기
                Max = ret
 
    print(f'#{test_case} {Max}')