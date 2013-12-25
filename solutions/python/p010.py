"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import utils


def run():
    """
    Solution: Use a prime sieve which I wrote in a separate file for
    reusability.
    """
    N = 2000000
    sieve = utils.get_prime_sieve(N)
    return sum([i if p else 0 for i, p in enumerate(sieve)])
