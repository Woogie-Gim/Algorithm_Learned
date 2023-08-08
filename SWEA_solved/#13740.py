# 13740 회문(string)
# 앞으로 읽어도 거꾸로 읽어도 같은 문자 찾기
# 2차원 배열에서 좌표를 기준으로 슬라이싱을 통해 가로 세로에 특정 길이의 문자를 출력
# 슬라이싱을 활용해 앞으로 읽어도 거꾸로 읽어도 같은지 확인

T = int(input())
 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [(list(map(str, input()))) for i in range(N)]
 
    result = []
    for k in range(N):
        for l in range(N):
            if k + M > N or l + M > N:
                continue
            ans = ''.join(arr[k][l : l + M])
            result.append(ans)
            ans2 = ''.join(arr[m][k] for m in range(l, l + M))
            result.append(ans2)
 
    for a in range(N - M + 1, N):
        for b in range(N):
            if b + M > N:
                continue
            ans3 = ''.join(arr[m][a] for m in range(b, b + M))
            result.append(ans3)
 
    for r in range(N - M + 1, N):
        for c in range(N):
            if c + M > N:
                continue
            ans4 = ''.join(arr[r][c : c + M])
            result.append(ans4)
 
    ans = ''
    for a in result:
        if a == a[::-1]:
            ans = a
 
    print(f'#{test_case} {ans}')