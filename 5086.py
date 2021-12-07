#z0mk1ng_BAEKJOON_5086

result = []

while(True):
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break

    if x % y == 0:
        result.append('multiple')
    elif y % x == 0:
        result.append('factor')
    else:
        result.append('neither')

for i in result:
    print(i)