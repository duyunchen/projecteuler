"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def run():
    """
    Yay for python having no integer overflow issues
    """
    return sum(map(int, str(2 ** 1000)))
