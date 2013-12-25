"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def run():
    """
    Solution: I'm going with a brute force-ish solution which still runs
    decently fast given the nature of the input.
    """
    SUM = 1000
    for a in xrange(1, 500):
        for b in xrange(a, SUM):
            c = SUM - a - b
            if a * a + b * b == c * c:
                return a * b * c
