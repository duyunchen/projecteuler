"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from utils import gcd

"""
Solution: Since we are dealing with only 2 digit numbers,
a brute force search is not so bad.
"""
def run():
    top, bottom = 1, 1
    
    for d in xrange(10, 100):
        for n in xrange(10, d):
            # extract digits as strings
            ns, ds = set(str(n)), set(str(d))
            
            # we need exactly one overlap
            if len(ds) is 1 or len(ns) is 1: continue
            
            # skip if there are no shared digits or if shared 0
            common = ds.intersection(ns)
            if len(common) is not 1 or str(0) in common: continue
            
            # compute the new fraction after removal of common digit
            denominator = float("".join(ds.difference(common)))
            if denominator < 1: continue
            numerator = float("".join(ns.difference(common)))
            
            # compare it to the original fraction
            a = float(n) / float(d)
            b = numerator/denominator
            if abs(a - b) < 0.000001:
                top *= n
                bottom *= d
    
    return bottom / gcd(top, bottom)
            
