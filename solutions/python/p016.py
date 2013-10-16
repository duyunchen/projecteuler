"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

# Yay for python no integer overflow issues
def run():
    return sum(map(int, str(2**1000)))