"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from utils import get_prime_sieve, is_prime

N = 10 ** 4
sieve = get_prime_sieve(N)


def run():
    """
    I can't think of a great way to do this other than just brute force.
    Generate all valid pairs of primes and compute intersections.
    This is EXTERMELY slow but still under 1 minute.
    """

    pairs = {}
    for p1 in xrange(N):
        if not sieve[p1]:
            continue

        if p1 not in pairs:
            pairs[p1] = generate_pairs(p1)

        for p2 in pairs[p1]:
            if p2 not in pairs:
                pairs[p2] = generate_pairs(p2)

            intersect = pairs[p1].intersection(pairs[p2])
            if len(intersect) is 0:
                continue

            for p3 in intersect:
                if p3 not in pairs:
                    pairs[p3] = generate_pairs(p3)

                intersect2 = pairs[p3].intersection(intersect)

                if len(intersect2) is 0:
                    continue

                for p4 in intersect2:
                    if p4 not in pairs:
                        pairs[p4] = generate_pairs(p4)

                    intersect3 = pairs[p4].intersection(intersect2)

                    if len(intersect3) is 0:
                        continue

                    return p1 + p2 + p3 + p4 + min(intersect3)


def generate_pairs(p):
    pairs = set()
    for p2 in xrange(p + 2, N, 2):
        if not sieve[p2]:
            continue
        if is_pair(p, p2):
            pairs.add(p2)
    return pairs


pair_cache = {}
prime_cache = {}


def is_pair(p1, p2):
    if p1 > p2:
        temp = p1
        p1 = p2
        p2 = temp

    if (p1, p2) not in pair_cache:
        if prime(int(str(p1) + str(p2))) and prime(int(str(p2) + str(p1))):
            pair_cache[(p1, p2)] = True
        else:
            pair_cache[(p1, p2)] = False
    return pair_cache[(p1, p2)]


def prime(n):
    if n not in prime_cache:
        if n > len(sieve):
            prime_cache[n] = is_prime(n)
        else:
            prime_cache[n] = sieve[n]
    return prime_cache[n]
