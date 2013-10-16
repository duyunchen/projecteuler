"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from utils import all_equal

# Basically loop till we find it
def run():
    number = 1
    while True:
        number += 1
        
        # Optimization
        if len(str(6 * number)) > len(str(number)):
            continue
        
        if all_equal([set(str(i * number)) for i in xrange(1, 7)]):
            return number
    
        
        
