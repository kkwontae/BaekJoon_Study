a, b = map(int, input().split())
c = int(input())

a = a+((b+c)//60)
b = b+(c%60)

if a>23:
    a = a-24
if b>59:
    b = b-60

print(a,b)