"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
import utils


def run():
    """
    Solution: Some basic dynamic programming
    """
    MAX = 20
    numbers = [1 for _ in xrange(MAX + 1)]  # stores subproblem solutions

    for i in xrange(2, MAX + 1):
        gcd = utils.gcd(numbers[i - 1], i)
        numbers[i] = numbers[i - 1] * i / gcd

    return numbers[MAX]
