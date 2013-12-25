"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the
following expression.

d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
"""


def run():
    """
    Solution: Use a generator to generate the digits
    """
    count, product, want = 1, 1, 1
    for n in generate_digits():
        if count == want:
            product *= n
            want *= 10
        if count == 1000000:
            break
        count += 1
    return product


def generate_digits():
    n = 1
    while True:
        for s in str(n):
            yield int(s)
        n += 1
