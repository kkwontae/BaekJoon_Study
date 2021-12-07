#z0mk1ng_BAEKJOON_10886

vote = []
N = int(input())

for i in range(N):
    vote.append(int(input()))

notcute = vote.count(0)
cute = vote.count(1)

if notcute > cute:
    print('Junhee is not cute!')
elif notcute < cute:
    print('Junhee is cute!')