"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from utils import get_divisors

# Another exercise in following specific given rules. Not the most efficient but works.
def run():
    MAX = 28123
    abundants = get_abundant_numbers(MAX)
    
    # The desired total
    numbers = range(MAX)
    
    # Subtract out all number able to be expressed as sum of abundant numbers
    for i in xrange(len(abundants)):
        for j in xrange(i, len(abundants)):
            if abundants[i] + abundants[j] < MAX:
                numbers[abundants[i] + abundants[j]] = 0
            else: break
                    
    return sum(numbers)
    
# Returns all abundant numbers less than a limit
def get_abundant_numbers(limit):
    return [number for number in xrange(12,limit) if sum(get_divisors(number)) > 2*number]