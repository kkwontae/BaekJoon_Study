#z0mk1ng_BAEKJOON_2754

score = input()

if score == 'A+':
    answer = 4.3
elif score == 'A0':
    answer = 4.0
elif score == 'A-':
    answer = 3.7
elif score == 'B+':
    answer = 3.3
elif score == 'B0':
    answer = 3.0
elif score == 'B-':
    answer = 2.7
elif score == 'C+':
    answer = 2.3
elif score == 'C0':
    answer = 2.0
elif score == 'C-':
    answer = 1.7
elif score == 'D+':
    answer = 1.3
elif score == 'D0':
    answer = 1.0
elif score == 'D-':
    answer = 0.7
elif score == 'F':
    answer = 0.0
else:
    answer = 0

print(answer)


def others():
    m = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0}
    print(m[input()])