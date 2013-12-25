"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from utils import factorial


def run():
    """
    Solution: Brute force search with a heuristic upper bound.

    What's the largest number beyond which this property cannot hold?

    I don't know enough number theory to procure a tight bound, but we can get
    one that's computationally good enough.

    Heuristic: Since every digit can at most contribute 9! = 362880 to the sum,
    beyond 6 digits the fac sum becomes increasingly unlikely to match the
    magnitude of the number since every additional digit only adds a relatively
    small 6 digit number to the sum.
    """
    N = 100000
    total = 0

    for n in xrange(3, N):
        if sum(map(lambda x: factorial(int(x)), str(n))) == n:
            total += n

    # sidenote: it turns out that only one other number besides the example
    #fits the given criteria.
    return total
