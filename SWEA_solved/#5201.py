T = int(input())
 
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    freight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    freight.sort(reverse = True)
    truck.sort()
    total = 0
 
    for i in truck:
        for j in range(len(freight)):
            if freight[j] <= i:
                total += freight[j]
                freight.pop(j)
                break
    print(f'#{test_case} {total}')