"""
Euler's Totient function, phi(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
relatively prime to nine, phi(9)=6.

n    Relatively Prime    phi(n)    n/phi(n)
2    1    1    2
3    1,2    2    1.5
4    1,3    2    2
5    1,2,3,4    4    1.25
6    1,5    2    3
7    1,2,3,4,5,6    6    1.1666...
8    1,3,5,7    4    2
9    1,2,4,5,7,8    6    1.5
10    1,3,7,9    4    2.5
It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""
from utils import gcd, get_prime_sieve
import math

N = 10 ** 6
cache = {1: 1}
sieve = get_prime_sieve(N)


def run():
    """
    Just a straightforward computation of phi for every number using

    https://en.wikipedia.org/wiki/Euler's_totient_function

    Some optimizations were used exploiting the properties of phi and some
    memoization and sieving.
    """
    max_ratio, max_value, = 0, 0
    for n in xrange(2, N + 1):
        ratio = n / float(compute_phi(n, sieve))
        if ratio > max_ratio:
            max_ratio = ratio
            max_value = n

    return max_value


def compute_phi(n, sieve=None):
    if n % 2 == 0:
        if n / 2 % 2 == 0:
            phi = 2 * cache[n / 2]
        else:
            phi = cache[n / 2]
    elif sieve and sieve[n]:
        phi = n - 1
    else:
        for a in xrange(2, int(math.sqrt(n)) + 1):
            if n % a == 0:
                b = n / a
                c = gcd(a, b)
                phi = cache[a] * cache[b] * c / cache[c]
                break
    cache[n] = phi
    return phi
