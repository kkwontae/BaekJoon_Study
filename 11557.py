#z0mk1ng_BAEKJOON_11557

T = int(input())

for i in range(T):
    N = int(input())
    Slist = []
    Llist = []
    SLdic = {}
    for j in range(N):
        S, L = input().split()
        Slist.append(S)
        Llist.append(int(L))
        SLdic[str(L)] = S
    Llist.sort()
    
    print(SLdic[str(Llist[len(Llist)-1])])