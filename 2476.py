#z0mk1ng_BAEKJOON_2476

T = int(input())

price = [0]*T

for i in range(T):
    dice = list(map(int, input().split()))
    dice.sort()
    
    if dice[0] == dice[2]:
        price[i] = 10000 + 1000*dice[2]
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        price[i] = 1000 + 100*dice[1]
    else:
        price[i] = 100*dice[2]

price.sort()
print(price[T-1])