#z0mk1ng_BAEKJOON_2753

yy = int(input())

if yy%4 == 0 and (yy%100 != 0 or yy%400 == 0):
    print(1)
else:
    print(0)