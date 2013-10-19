"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from utils import get_prime_sieve

"""
Solution: Make a boolean list indexed by natural numbers -> true if the number
fulfills the requirements and odd otherwise.  We can use our prime number sieve
to filter out the primes
"""
def run():
    N = 10000
    
    n = get_prime_sieve(N)
    p = n[:]
    
    for a in xrange(N + 1):
        if a == 1 or a % 2 == 0:
            n[a] = True
            continue
        for b in xrange(N):
            if p[a] and a + 2*b*b < N:
                n[a + 2*b*b] = True
    
    return n.index(False)
                
        
        