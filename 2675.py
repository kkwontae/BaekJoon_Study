#z0mk1ng_BACKJOON_5355

T = int(input())

for i in range(T):
    R, S = input().split()
    P = ""
    for j in S:
        for k in range(int(R)):
            P += j
    print(P)