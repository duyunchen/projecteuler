"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


#Solution: a simple list comprehension does the trick.
def run():
    return sum([0 if i % 3 and i % 5 else i for i in xrange(1000)])
