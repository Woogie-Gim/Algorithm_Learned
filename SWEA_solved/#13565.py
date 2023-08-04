# 13565 전기버스

T = int(input()) # 테스트 케이스 입력 받기

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    bucket = [0] * (N + 1)

    for i in range(len(arr)):
        bucket[arr[i]] += 1
    # bucket을 이용하여 충전소 위치를 표시

    s = 0
    e = K
    cnt = 0
    # 투포인터를 활용하여 버스를 출발 시켜 K 만큼 이동 후 그 사이에 충전소가 있는지 확인
    while e < N: # 포인터가 리스트 끝에 가기 전에 반복문 종료
        while e > s and bucket[e] == 0:
            e -= 1
        # 만약에 버스가 이동거리만큼 갔을 때 0 이라면 충전소가 없기 때문에 e를 1칸 앞으로 이동하여 충전하기
        if e == s:
            cnt = 0
            break
        # e와 s는 겹치지 않는다
        cnt += 1 # 충전 횟수 추가
        s = e # 버스가 이동 가능 거리만큼 이동
        e = s + K # 버스 이동 후 이동 거리 만큼 이동 했을 때 충전소가 있는지 확인

    print(f'#{test_case} {cnt}')