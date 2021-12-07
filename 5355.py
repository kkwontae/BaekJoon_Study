#z0mk1ng_BACKJOON_5355

T = int(input())

for i in range(int(T)):
    listA = list(map(str, input().split()))    
    
    result = float(listA[0])

    for i in range(1,len(listA)):
        if listA[i] == '@':
            result *= 3
        elif listA[i] == '%':
            result += 5
        elif listA[i] == '#':
            result -= 7
        else:
            print('err')

    print("%.2f" % result)