"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def run():
    """
    Brute force galore and still pretty fast
    """
    count = 0
    for n in xrange(1, 100):
        a = 1
        power = 1
        while len(str(power)) <= n:
            power = a ** n

            if len(str(power)) == n:
                count += 1
            a += 1
    return count
