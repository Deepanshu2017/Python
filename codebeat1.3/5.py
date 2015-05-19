__author__ = 'deepanshu'

number = 1234567
prime_gar = [j for j in range(0, number)]

for i in range(2, number):
    if prime_gar[i]:
        j = i + i
        while j < number:
            prime_gar[j] = 0
            j += i

T = int(raw_input())
for _ in range(T):
    if prime_gar[int(raw_input())]:
        print 'YES'
    else:
        print 'NO'