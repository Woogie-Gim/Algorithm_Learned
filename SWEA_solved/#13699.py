T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    my_arr = [(list(map(int, input().split()))) for i in range(N)]
    arr = [[0] * 10 for i in range(10)]
 
    for k in range(N):
        for i in range(my_arr[k][0], my_arr[k][2] + 1):
            for j in range(my_arr[k][1], my_arr[k][3] + 1):
                arr[i][j] += my_arr[k][4]
 
    cnt = 0
 
    for a in range(10):
        for b in range(10):
            if arr[a][b] >= 3:
                cnt += 1
 
    print(f'#{test_case} {cnt}')

# Direct 활용해서 1이나 2 색으로 칠하고 겹치는 부분은 더해서
# 3 이상일 경우 카운트를 올린다