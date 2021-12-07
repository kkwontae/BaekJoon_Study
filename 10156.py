#z0mk1ng_BAEKJOON_10156

K, N, M = map(int, input().split())

need = K*N-M
if need < 0:
    need = 0
print(need)