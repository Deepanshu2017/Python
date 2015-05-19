__author__ = 'deepanshu'

T = int(raw_input())

for i in range(0, T):
    N, M = raw_input().split()
    res = ""
    mini = min(len(N), len(M))
    for j in range(0, mini):
        res = res + str(int(N[j]) + int(M[j]))
    for j in range(mini, len(N)):
        res = res + str(N[j])
    for j in range(mini, len(M)):
        res = res + str(M[j])
    print res
