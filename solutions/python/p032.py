"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from utils import generate_perm


def run():
    """
    Solution: Resorting to brute force with optimizations

    The trick is to realize that the only way we can have a
    pandigital product is 2-dig * 3-dig = 4-dig or
    1-dig * 4-dig = 4-dig
    """
    used = set()
    total = 0
    # look through all permutations of digits
    # and check for 2-3-4 or 1-4-4 product patterns
    for perm in generate_perm("123456789"):
        c1 = check_234(perm)
        c2 = check_144(perm)
        if c1 and c1 not in used:
            used.add(c1)
            total += c1
        if c2 and c2 not in used:
            used.add(c2)
            total += c2
    return total


def check_234(perm):
    a = int(perm[0:2])
    b = int(perm[2:5])
    c = int(perm[5:9])
    return c if a * b == c else 0


def check_144(perm):
    a = int(perm[0:1])
    b = int(perm[1:5])
    c = int(perm[5:9])
    return c if a * b == c else 0
