"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
 by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
 (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from utils import generate_perm, get_prime_sieve


def run():
    """
    Solution: Brute force.  I already wrote a lot of the tools needed for this.
    """
    # optimization: use a prime sieve
    is_prime = get_prime_sieve(9999)

    for n in xrange(1000, 10000):
        nums = set()
        for s in generate_perm(str(n)):
            if is_prime[int(s)]:
                nums.add(int(s))

        if len(nums) < 3:
            continue

        seq = contains_arithmetic_sequence(nums)
        if seq:
            result = str(seq[0]) + str(seq[1]) + str(seq[2])
            if len(result) == 12 and result != "148748178147":
                return result


def contains_arithmetic_sequence(sequence):
    """
    Detemines if a set contains an arithmetic progression of
    length 3 by using brute force once again
    """
    for a in sequence:
        for b in sequence:
            if a == b:
                continue
            if a + 2 * (b - a) in sequence:
                return a, b, a + 2 * (b - a)
    return None
