"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n  1?
"""


def run():
    """
    Solution: Just a brute force search with some optimizations.
    We only need to check up to 9876 because any more than that the
    concatenation will result in a 10 digit number since n > 1
    """
    largest = 0
    for n in xrange(1, 9877):

        concat = ""
        multiplier = 1
        while len(concat) < 9:
            concat += str(n * multiplier)
            multiplier += 1

        if len(concat) != 9 or "0" in concat or len(set(concat)) != 9:
            continue

        if int(concat) > largest:
            largest = int(concat)

    return largest
