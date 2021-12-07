#z0mk1ng_BAEKJOON_3009

x = list()
y = list()

answer = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        answer.append(i)

for i in y:
    if y.count(i) == 1:
        answer.append(i)

print('{0} {1}'.format(answer[0],answer[1]))