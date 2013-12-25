"""
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

from utils import combination


def run():
    """
    This is more of a math question.  In an a x b grid there are [(a+b)
    choose a] routes. Another useful util function for later.
    """
    return combination(40, 20)
