"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import get_prime_sieve

"""
Solution: Just a brute force search with some optimizations.
"""
def run():
    N = 11 #how many desired truncatable primes
    
    #optimization: use a prime sieve
    sieve = get_prime_sieve(10**6)
    
    count, total, n = 0,0,11
    while count < N:
        n += 2
        if not sieve[n]: 
            continue
        
        ns = str(n)
        # the number 100% cannot be truncatable if these are not met
        if ns[0] == "9" or ns[:-1] == "9": continue
        if len(set("0468").intersection(set(ns))) > 0: continue
        
        #check truncatability
        for i in xrange(1, len(ns)):
            p1 = int(ns[i:])
            if not sieve[p1]: break
            p2 = int(ns[:i])
            if not sieve[p2]: break
        else:
            count += 1
            total += n
            
    return total