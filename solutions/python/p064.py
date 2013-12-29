"""
How many continued fractions for N <= 10000 have an odd period?
"""
from math import sqrt


def run():
    """
    The trick to finding the period is realizing what rules have to be
    followed and when to stop the recursion (e.g. when is a period detected).
    """
    count = 0
    for n in xrange(2, 10001):
        if len(coefficients(n, int(sqrt(n)), 1)) % 2 == 1:
            count += 1
    return count


def coefficients(n, a, b, first=None):
    b = float((n - a * a) / b)
    if b == 0:
        return []
    c = int((sqrt(n) + a) / b)
    a = c * b - a
    if not first:
        first = (a, b)
    else:
        if (a, b) == first:
            return []
    return [c] + coefficients(n, a, b, first)
