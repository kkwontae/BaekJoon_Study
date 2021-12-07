#z0mk1ng_BAEKJOON_10988

string = input()
gnirts = ''

for i in range(len(string)-1, -1, -1):
    gnirts += string[i]

if string == gnirts:
    print(1)
else:
    print(0)

## string = input()
## gnirts = string[::-1]
##
## < Extended Slices >
## string [ start : end : interval ]