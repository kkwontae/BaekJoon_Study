#z0mk1ng_BAEKJOON_9506

while(True):
    n = int(input())
    result = str(n)
    if n == -1:
        break
    
    lcm = []
    for i in range(1, n):
        if n%i==0:
            lcm.append(i)
    if sum(lcm) != n:
        result += ' is NOT perfect.'
    else:
        result += ' = '
        for item in lcm:
            if lcm.index(item) == len(lcm) - 1:
                result += str(item)
            else:
                result += str(item) + ' + '
    print(result)
