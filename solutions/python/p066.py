"""
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2*2^2 = 1
2^2 - 3*1^2 = 1
9^2 - 5*4^2 = 1
5^2 - 6*2^2 = 1
8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""


def run():
    """
    Some ancient indian number theory to the rescue.

    https://en.wikipedia.org/wiki/Chakravala_method
    http://cs.annauniv.edu/insight/Reading/algebra/indet/chakra.htm
    """

    highest = 0
    highest_D = 0
    for D in xrange(2, 1001):
        x, _ = chakravala(D, 1, 1, 1, 0)
        if x and x > highest:
            highest = x
            highest_D = D

    return highest_D


def chakravala(D, p, k, x, y):
    if k == 0:
        return None, None

    # choose best pr
    pr, prev = 0, 0
    while True:
        pr += 1
        if (p + pr) % abs(k) != 0:
            continue
        if D >= prev * prev and D <= pr * pr:
            pr = prev if D - prev * prev < pr * pr - D else pr
            break
        prev = pr

    kr = (pr * pr - D) / k
    xr = (pr * x + D * y) / abs(k)
    yr = (pr * y + x) / abs(k)

    if kr == 1:
        return xr, yr
    else:
        return chakravala(D, pr, kr, xr, yr)
