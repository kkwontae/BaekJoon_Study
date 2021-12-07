#z0mk1ng_BAEKJOON_1934
def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b/gcd(a,b)

T = int(input())

c = [0]*T

for i in range(T):
    a, b = map(int, input().split())
    c[i] = int(lcm(a,b))

for i in c:
    print(i)