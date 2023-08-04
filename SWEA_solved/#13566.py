T = int(input()) # 테스트 케이스 입력 받기
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
 
    bucket = [0] * 10 
 
    for i in range(N):
        bucket[arr[i]] += 1
    # 버켓을 활용하여 각 카드의 개수를 bucket 인덱스를 통해서 표시
    Max = -21e8
    Max_index = -21e8
 
    for j in range(len(bucket)):
        if bucket[j] >= Max: # >= 를 통해서 개수가 같다면 높은 숫자의 카드를 출력
            Max = bucket[j]
            Max_index = j
    # 카드 숫자의 최대 값과 무슨 카드인지 확인
 
    print(f'#{test_case} {Max_index} {Max}')