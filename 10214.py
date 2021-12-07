#z0mk1ng_BAEKJOON_10214

T = int(input())

for i in range(T):
    Ys = Ks = 0
    for i in range(9):
        Y, K = map(int, input().split())
        Ys += Y
        Ks += K
    if Ys < Ks:
        print('Korea')
    elif Ys > Ks:
        print('Yonsei')
    else:
        print('Draw')