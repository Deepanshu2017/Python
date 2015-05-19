__author__ = 'deepanshu'

T = int(raw_input())
for _ in range(T):
    N = int(raw_input())
    sum = 0
    while N:
        sum += N % 10
        N /= 10

    print sum