# Given a non-negative integer n, return the nth number in the Fibonacci sequence.
# Constraints 0 <= n <= 30
# The sequence is: Index: 0 1 2 3 4 5 6 7 8 9 Value: 0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b