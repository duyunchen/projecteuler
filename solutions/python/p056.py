"""
A googol (10100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""

from utils import digit_sum


def run():
    """
    Brute force with some simple optimizations.  We know that b should be large
    because more digits = higher sum.  We'll limit search of b between 90 and
    100.  a can't be too small either.  We'll search a from 50 up.
    """
    max_sum = 0
    for a in xrange(50, 100):
        if a % 10 is 0:
            continue
        for b in xrange(90, 100):
            s = digit_sum(a ** b)
            if s > max_sum:
                max_sum = s

    return max_sum
