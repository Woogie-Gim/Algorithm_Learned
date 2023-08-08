# 13749 어디에 단어가 들어갈 수 있을까
# 2차원 배열을 입력받아 원하는 길이의 문자 찾기
# 2차원 배열의 좌표를 탐색하여 좌표를 기준으로 가로 / 세로 별로 슬라이싱을 통해 특정 길이의 문자열 찾기
# 단, 1로만 이루어진 문자열이기 때문에 1111 등 겹칠 수 있는 문자열은
# 입력 받은 전문자열, 이후문자열과 비교하여 같을 경우 리스트에 추가하지 않는 방식으로 진행

T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [(list(map(str, input().split()))) for i in range(N)]
 
    result = []
    for k in range(N):
        for l in range(N):
            if l + M > N or k + M > N:
                continue
            a1 = l + 1 + M
            if a1 > N:
                a1 = a1 - 1
            a2 = l - 1
            if a2 < 0:
                a2 = a2 + 1
            ans = ''.join(arr[k][l : l + M])
            afterans = ''.join(arr[k][l + 1: a1])
            beforeans = ''.join(arr[k][l - 1: a2 + M])
            if ans != afterans and ans != beforeans:
                result.append(ans)
            ans2 = ''.join(arr[m][k] for m in range(l, l + M))
            afterans2 = ''.join(arr[m][k] for m in range(l + 1, a1))
            beforeans2 = ''.join(arr[m][k] for m in range(l - 1, a2 + M))
            if ans2 != afterans2 and ans2 != beforeans2:
                result.append(ans2)
 
    for a in range(N - M + 1, N):
        for b in range(N):
            if b + M > N + 1 or b + 1 + M > N + 1:
                continue
            a3 = b + 1 + M
            if a3 > N:
                a3 = a3 - 1
            a4 = b - 1
            if a4 < 0:
                a4 = a4 + 1
            ans3 = ''.join(arr[m][a] for m in range(b, b + M))
            afterans3 = ''.join(arr[m][a] for m in range(b + 1, a3))
            beforeans3 = ''.join(arr[m][a] for m in range(b - 1, a4 + M))
            if ans3 != afterans3 and ans3 != beforeans3:
                result.append(ans3)
 
    for r in range(N - M + 1, N):
        for c in range(N):
            if c + M > N:
                continue
            k = c + 1 + M
            a5 = c + 1 + M
            if a5 > N:
                a5 = a5 - 1
            a6 = c - 1
            if a6 < 0:
                a6 = a6 + 1
            ans4 = ''.join(arr[r][c: c + M])
            afterans4 = ''.join(arr[r][c + 1: a5])
            beforeans4 = ''.join(arr[r][c - 1: a6 + M])
            if ans4 != afterans4 and ans4 != beforeans4:
                result.append(ans4)
 
    ans = '1' * M
    cnt = 0
    for i in result:
        if i in ans:
            cnt += 1
 
    print(f'#{test_case} {cnt}')