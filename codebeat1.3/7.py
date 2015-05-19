__author__ = 'deepanshu'

T = int(raw_input())
for i in range(0, T):
    M = int(raw_input())
    lst = map(int, raw_input().split())
    N = lst.pop(0)
    lst.sort()
    j = N - 1
    i = 0
    res = 0
    while ( i <= j):
        if(lst[j] > M):
            j -= 1
        elif(lst[i] + int(lst[j]) > M):
            j -= 1
            res += 1
        else:
            i += 1
            j -= 1
            res += 1
    print res