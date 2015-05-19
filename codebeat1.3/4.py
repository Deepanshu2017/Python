__author__ = 'deepanshu'

T = int(raw_input())
for _ in range(T):
    N = int(raw_input())
    temp = N % 9
    if temp:
        print temp
    else:
        print 9