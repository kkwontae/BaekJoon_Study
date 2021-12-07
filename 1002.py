#z0mk1ng_BAEKJOON_1002

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    if r1+r2 < d:
        print(0)
        continue
    if r1-r2 > d or r2-r1 > d:
        print(0)
        continue
    if d==0:
        if r1 != r2:
            print(0)
        else:
            print(-1)
        continue
    if r1+r2 == d:
        print(1)
        continue
    if r1-r2 == d or r2-r1 == d:
        print(1)
        continue
    if (r1-r2 < d or r2-r1 < d) and r1+r2 > d:
        print(2)
        continue
