#z0mk1ng_BAEKJOON_4101

answer = list()

while True:
    a, b = map(int, input().split())
    if a > b:
        answer.append('Yes')
    else:
        if a==0 and b==0:
            break
        else:
            answer.append('No')

for i in answer:
    print(i)