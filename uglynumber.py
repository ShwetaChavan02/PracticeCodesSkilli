# ugly number
# An ugly number is a positive integer whose prime factors are only 2, 3, and 5.
# Given an integer n, determine whether n is an ugly number.
# To check this, repeatedly divide n by 2, 3, and 5 as long as it is completely divisible by them. 
# After removing all possible factors:
# If the remaining value is 1, then n is an ugly number. 
# If the remaining value is greater than 1, then n has another prime factor and is not an ugly number. 
# Any n <= 0 is not an ugly number.

class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        return n == 1