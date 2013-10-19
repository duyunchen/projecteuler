"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from utils import get_prime_factors, get_prime_sieve

"""
Solution: Brute force
"""
def run():
    first, consec = 0,0
    n = 647
    first = 0
    
    while consec < 4:
        factors = get_prime_factors(n)
        if len(factors) == 4:
            if consec == 0: first = n
            consec += 1
        else:
            consec = 0
            first = 0
        n += 1
    
    return first

        
        