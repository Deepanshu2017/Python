"""
Newton's Method
Estimate x = N / 2 + 1
and Y = (X + N / X ) / 2
then loop ove untill Y >= X
"""

def newton_method(N):
    X = N / 2 + 1
    while True:
        Y = (X + N / X) / 2
        if Y >= X:
            return X
        X = Y


N = int(raw_input())
N = N * 1.0
print newton_method(N)
