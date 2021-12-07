#z0mk1ng_BAEKJOON_9610

n = int(input())
dic = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}
for i in range(n):
    x, y = map(int, input().split());
    #r1, r2, r3, r4, axis = 0

    if x>0 and y>0:
        dic['Q1'] = dic['Q1'] + 1
    elif x<0 and y>0:
        dic['Q2'] = dic['Q2'] + 1
    elif x<0 and y<0:
        dic['Q3'] = dic['Q3'] + 1
    elif x>0 and y<0:
        dic['Q4'] = dic['Q4'] + 1
    else:
        dic['AXIS'] = dic['AXIS'] + 1

print('Q1: {}'.format(dic['Q1']))
print('Q2: {}'.format(dic['Q2']))
print('Q3: {}'.format(dic['Q3']))
print('Q4: {}'.format(dic['Q4']))
print('AXIS: {}'.format(dic['AXIS']))