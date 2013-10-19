"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils import is_prime, generate_perm

"""
Solution: Simple brute force using tools written for previous problems.

I somewhat cheated here because I established a priori that 8- and 9-digit
pandigital primes cannot exist by running the algorithm below on those digit
strings.

A true algorithm should establish that fact within a single run, but I think
this problem is not interesting enough to warrant any further effort.
"""
def run():
    for n in generate_perm("7654321"):
        if is_prime(int(n)):
            return int(n)