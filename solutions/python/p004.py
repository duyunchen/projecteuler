"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils import is_palindrome


def run():
    """
    Solution: just a double loop through all 3-digit numbers and check
    if the product is palindrome while keeping track of the largest.
    """
    largest = 0
    for a in xrange(100, 1000):
        for b in xrange(100, 1000):
            p = a * b
            if is_palindrome(p) and p > largest:
                largest = p
    return largest
