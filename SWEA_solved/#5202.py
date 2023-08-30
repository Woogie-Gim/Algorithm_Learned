def count(start, end, cnt):
    global Max
    if cnt > Max:
        Max = cnt
    if end == 24:
        return
 
    for i in range(n):
        if visited[i] == 0:
            new_s = start
            new_e = end
            if end <= ans[i][0]:
                visited[i] = 1
                start = ans[i][0]
                end = ans[i][1]
                count(start, end, cnt + 1)
                visited[i] = 0
                start = new_s
                end = new_e
 
T = int(input())
 
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])
    visited = [0] * n
    ans = sorted(arr, key = lambda x : (x[0], x[1]))
 
    Max = -21e8
    for i in ans:
        count(i[0], i[1], 1)
 
    print(f'#{test_case} {Max}')