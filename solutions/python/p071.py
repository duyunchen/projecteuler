"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <= 1,000,000 in ascending
order of size, find the numerator of the fraction immediately to the left of
3/7.

"""
from utils import gcd


def run():
    """
    Iterate through all denominators d, then descend through numerators n
    less than 3d/7 until gcd(n,d) = 1 (reduced proper fraction). The largest
    n / d fraction obtained in this fashion for some d is the answer we are
    looking for.

    Alternatively, just realize that 7 divides 999999 evenly so the answer
    must be 999999 * 3/7 - 1.  No other fraction with d < 1000000 is closer to
    3/7 than this number.
    """
    bn, bd = 0, 1
    for d in xrange(8, 1000000):
        n = int(3 * d / 7.0)
        while gcd(n, d) > 1:
            n -= 1
        if n * bd > d * bn:
            bn = n
            bd = d
    return bn
