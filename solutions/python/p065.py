"""
It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for sqrt(2).

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
"""
from utils import gcd


def run():
    """
    Just follow the rules.  Pretty straightforward
    """
    e = [2]
    k = 1
    while len(e) < 1022:
        e += [1, 2 * k, 1]
        k += 1

    n, _ = convergent(e, 99)
    return sum(map(int, str(n)))


def convergent(coeffs, N):
    if N == 0:
        return coeffs[0]
    n, d = 0, 0
    while N > 0:
        c = coeffs[N]
        if d is 0:
            n = 1
            d = c
        else:
            temp = n
            n = d
            d = temp + c * d
        N -= 1
    n = coeffs[0] * d + n
    g = gcd(n, d)
    return n / g, d / g
