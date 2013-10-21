"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

"""
Solution: This almost feels like cheating.  I love you python.
"""
def run():
    return sum(map(lambda x: x ** x, range(1,1001))) % 10 ** 10

        
