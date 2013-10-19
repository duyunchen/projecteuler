"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from utils import is_palindrome, to_binary

"""
Solution: Pretty straightforward search.
"""
def run():
    N = 1000000
    
    total = 0
    for n in xrange(1, N):
        if not is_palindrome(n): continue
        
        if is_palindrome(to_binary(n)):
            total += n
    return total