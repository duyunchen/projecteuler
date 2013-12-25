"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from utils import get_prime_list


def run():
    """
    Solution: Brute force by first computing the cumulative sum
    of the first n primes.  Any consecutive prime between the
    ith and jth prime can be expressed as cum_sum[j] - cum_sum[i].
    """
    N = 1000000
    primes = get_prime_list(N)
    prime_set = set(primes)
    cum_sum = [0 for i in xrange(1, len(primes) + 1)]
    for i in xrange(1, len(primes)):
        cum_sum[i] = primes[i] + cum_sum[i - 1]

    longest, best = 21, 953

    for i in xrange(len(primes)):
        for j in xrange(i - longest):
            l = i - j
            n = cum_sum[i] - cum_sum[j]
            if l <= longest or n > N:
                break
            if n in prime_set:
                longest = l
                best = n

    return best
