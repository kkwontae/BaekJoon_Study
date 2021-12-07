#z0mk1ng_BACKJOON_11653

a = int(input())

if a==1:
    print(1)
else:
    for i in range(2,int(a**0.5)):
        while a%i == 0:
            print(i)
            a //= i

    if a > 1:
        print(a)
