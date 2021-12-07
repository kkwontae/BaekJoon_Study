#z0mk1ng_BAEKJOON_10039

stu = [0]*5
sum = 0

for i in range(5):
    stu[i] = int(input())
    if stu[i] < 40:
        stu[i] = 40

    sum += stu[i]
print(int(sum/5))