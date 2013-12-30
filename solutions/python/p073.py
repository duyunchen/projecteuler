"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d <= 12,000?

"""


def run():
    """
    Farey sequence to the rescue.

    https://en.wikipedia.org/wiki/Farey_sequence

    This basically says that given two consecutive fractions in a sorted
    sequence like the kind we are dealing with (with bounded denominator),
    you can compute the next fraction in the sequence.

    So we take 1/3 and use a similar algorithm from p071 to find the
    next fraction, then apply farey to find consecutive fractions until 1/2
    is reached.  I precomputed the next fraction, which is 4000/11999.
    """

    result, a, b, n, d = 0, 1, 3, 4000, 11999

    while (n, d) != (1, 2):
        result += 1
        k = (12000 + b) / d
        t1, t2 = k * n - a, k * d - b
        a, b, n, d = n, d, t1, t2

    return result
