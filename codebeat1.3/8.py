__author__ = 'deepanshu'


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

T = int(raw_input())
for _ in range(T):
    a, b = map(int, raw_input().split())
    print( gcd(a, b) )