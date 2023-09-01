def dfs(index, count) :
    global ans
    if count == int(cnt) :
        ans = max(int(''.join(data)), ans)
        return
    for now in range(index, len(data)) :
        for max_idx in range(now + 1, len(data)) :
            if data[now] <= data[max_idx] :
                data[now], data[max_idx] = data[max_idx], data[now]
                dfs(now, count + 1)
                data[now], data[max_idx] = data[max_idx], data[now]

    if ans == 0 and count < int(cnt) :
        extra = (int(cnt) - count) % 2
        if extra == 1 :
            data[-1], data[-2] = data[-2], data[-1]
        dfs(index, int(cnt))

t = int(input())

for test_case in range(1, t + 1) :
    data, cnt = input().split()
    data = list(data)
    ans = 0
    dfs(0, 0)

    print(f'#{test_case} {ans}')