#z0mk1ng_BACKJOON_2530

h, m, s = map(int, input().split())
t = input()

second = h*60*60 + m*60 + s + int(t)

H = second // 3600 % 24
M = second // 60 % 60
S = second % 60

print(H,M,S)
