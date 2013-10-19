"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils import get_prime_sieve, generate_rotation

"""
Solution: This can be done with existing tools developed for previous
problems
"""
def run():
    N = 1000000
    #optimization: use a prime sieve for fixed bounds
    is_prime = get_prime_sieve(N) 
    count = 0
    for n in xrange(2, N):
        if not is_prime[n]: continue
        
        for rotation in generate_rotation(str(n)):
            if not is_prime[int(rotation)]:
                break 
        else:
            count += 1
    
    return count