T = int(input())
 
def card(player):
    for j in range(10):
        if player[j] == 3:
            return True
    for k in range(8):
        if player[k] and player[k + 1] and player[k + 2]:
            return True
    return False
 
 
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
 
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
 
    for i in range(len(arr)):
        if not i % 2:
            player1[arr[i]] += 1
            if card(player1):
                winner = 1
                break
        else:
            player2[arr[i]] += 1
            if card(player2):
                winner = 2
                break
 
    print(f'#{test_case} {winner}')