__author__ = 'deepanshu'


def prime(x):
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            return False
    return True


n = input()
inversion = 0
a = map(int, raw_input().split())
b = map(int, raw_input().split())
i = 0
j = 0
while i < len(a)-1:
    while i < j+1 and j < len(b):
        if a[i] > b[j]:
            inversion += 1
        j += 1
    i += 1
if prime(inversion):
    print 'MAGIC INVERSION'
else:
    print 'SIMPLE INVERSION'