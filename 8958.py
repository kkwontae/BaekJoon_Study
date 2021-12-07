#z0mk1ng_BAEKJOON_8958
 
T = int(input())

for i in range(T):
    string = input()
    result = 0
    count = 1
    for j in range(len(string)):
        if string[j] == 'O':
            if j > 0 and string[j-1] == 'O':
                count = count + 1
            else:
                count = 1
            result = result + count
    print(result)
        
            