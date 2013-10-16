"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

"""
Solution: Brute force again.  Not sure if there are number theory tricks to this.
"""
def run():
    #We loosely choose this as a cap.  Doesn't make sense to search above this
    #since 9999 < 4*9^5 < 900999.  Prob not a tight bound but it's acceptably
    #fast with this (< 1s).
    N = 4*(9**5)
    
    total = 0
    for n in xrange(2, N):
        s = sum(map(lambda x: int(x)**5, str(n)))
        if s == n:
            total += n

    return total
