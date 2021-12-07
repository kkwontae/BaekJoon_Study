#z0mk1ng_BAEKJOON_10162

T = int(input())

Ta = Tb = Tc = 0
if T>=300:
    Ta = T//300
    T %= 300
if T>=60:
    Tb = T//60
    T %= 60
if T>=10:
    Tc = T//10
    T %= 10

if T%10 != 0:
    print(-1)
else:
    print(Ta, Tb, Tc)