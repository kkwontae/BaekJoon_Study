#z0mk1ng_BAEKJOON_2884

H, M = map(int, input().split())

time = H * 60 + M - 45

if time < 0:
    time += 60*24

hour = time//60
minute = time%60

print(hour, minute)