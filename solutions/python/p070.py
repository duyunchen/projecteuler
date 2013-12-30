"""
See previous question.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and
the ratio n/phi(n) produces a minimum.

"""
from utils import get_prime_sieve
from itertools import combinations


def run():
    """
    n is getting too big to use the technique from p069 and still have it run
    within a minute.  So we have to make some assumptions and heuristics.

    n/phi(n) = n/(n * prod_(p|n)(1 - 1/p)) = 1/prod_(p|n)(1 - 1/p)

    To minimize the above we need to maximize prod_(p|n)(1 - 1/p).  Since
    1 - 1/p < 1, every term in the product makes the denominator smaller.
    Hence we probably want to minimize the number of terms while keeping it
    a composite number.  This leads to the heuristic that we are looking for
    a semiprime number of the form pq. Since p and q are coprime, we can use
    the multiplicative property of the phi function

    phi(n) = phi(p)phi(q) = (p - 1)(q - 1)

    Therefore n/phi(n) is minimized when (p - 1)(q - 1) is maximized. Since
    n < 10^7, we are probably looking for two four digit primes. Brute forcing
    this search space.
    """

    sieve = get_prime_sieve(10000)
    primes = [p for p, prime in enumerate(sieve) if prime and p > 1000]

    min_ratio = 2
    min_value = 0
    for (p1, p2) in combinations(primes, 2):
        n = p1 * p2
        if n >= 10000000:
            continue
        phi = (p1 - 1) * (p2 - 1)
        ratio = n / float(phi)
        if sorted(str(n)) == sorted(str(phi)) and ratio < min_ratio:
            min_ratio = ratio
            min_value = n

    return min_value
