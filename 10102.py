#z0mk1ng_BAEKJOON_10102

n = int(input())

vote = input()

a = vote.count('A')
b = vote.count('B')

if a < b:
    print('B')
elif a > b:
    print('A')
else:
    print('Tie')