#13761 가장 빠른 문자열 타이핑
# 문자열 메서드를 활용한 문제풀이

T = int(input())
 
for test_case in range(1, T + 1):
    a, b = map(str, input().split())
 
    cnt = a.count(b)
 
    c = a.replace(b, '')
    ans = cnt + len(c)
 
    print(f'#{test_case} {ans}')