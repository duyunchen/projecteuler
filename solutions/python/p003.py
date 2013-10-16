"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#Solution: just loop through and keep chopping the number down with small
#primes.  we skip all the even numbers because 600851475143 is odd.
def run():
    n = 600851475143
    i = 3
    largest = 0
    
    while n is not 1:
        while n % i is 0:
            n = n/i
            largest = i
        i += 2
    
    return largest

