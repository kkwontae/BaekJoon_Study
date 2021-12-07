#z0mk1ng_BAEKJOON_10103

n = int(input())

a = b = 100
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 < d2:
        a -= d2
    elif d1 > d2:
        b -= d1
print(a)
print(b)