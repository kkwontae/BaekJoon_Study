#z0mk1ng_BACKJOON_7287

h, m = map(int, input().split())
t = input()

minute = h*60 + m + int(t)

H = minute // 60 % 24
M = minute % 60

print(H,M)
