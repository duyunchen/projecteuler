"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import utils

# Solution: Pretty straight forward. Loop till we find the 10001th prime.
# The prime checking is the stardard modulus up to square root method
# that I wrote in a separate file because that code will be reused heavily
# in most of these types of problems.
def run():
    MAX = 10001
    index = 2
    number = 3
    while index < MAX:
        number += 2
        if utils.is_prime(number):
            index += 1
        
    return number