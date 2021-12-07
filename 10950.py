#z0mk1ng_BAEKJOON_10950

T = int(input())
answer = list()

for i in range(T):
    a, b = map(int, input().split())
    answer.append(a+b)

for i in range(T):
    print(answer[i])
