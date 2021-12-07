#z0mk1ng_BAEKJOON_2480

dice = list(map(int, input().split()))

dice.sort()
q = list(set(dice))
print(q)

if dice[0] == dice[2]:
    price = 10000 + 1000*dice[2]
elif dice[0] == dice[1] or dice[1] == dice[2]:
    price = 1000 + 100*dice[1]
else:
    price = 100*dice[2]

print(price)