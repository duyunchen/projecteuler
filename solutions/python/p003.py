"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def run():
    """
    Solution: just loop through and keep chopping the number down with small
    primes.  we skip all the even numbers because 600851475143 is odd.
    """
    n = 600851475143
    i = 3
    largest = 0
    while n != 1:
        while n % i == 0:
            n = n / i
            largest = i
        i += 2
    return largest
