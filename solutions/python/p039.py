"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
"""

from utils import Counter

"""
Solution: Just a brute force search with some optimizations.
"""
def run():
    counter = Counter()
    for a in xrange(3, 1000):
        for b in xrange(a + 1, 1000-a):
            for c in xrange(b + 1, min(a+b, 1000-(a+b))):
                if a*a + b*b == c*c:
                    counter.add(a + b + c)
    return counter.get_most()[0]