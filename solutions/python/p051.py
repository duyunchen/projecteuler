"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

from utils import Counter, get_prime_sieve


def run():
    """
    Brute force over all the primes, retroactively incrementing family member
    count of all related numbers.  Using a estimated upper bound of a million.
    """
    N = 10 ** 2
    primes = get_prime_sieve(N)
    counter = Counter()

    for p, is_prime in enumerate(primes):
        if not is_prime or p < 10:
            continue

        for digit in '0123456789':
            replaced = str(p)
            count = replaced.count(digit)

            while digit in replaced:
                replaced = replaced.replace(digit, '*', 1)
                counter.add(replaced)

    print counter.get_most()
    return None
