"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""


def run():
    """
    Go through all the cubes and index by sorted digits, until we see a set of
    5
    """
    S = {}
    for n in xrange(5, 10000):
        N = n * n * n
        index = ''.join(sorted(str(N)))

        if index not in S:
            S[index] = set()
        S[index].add(N)

        if len(S[index]) == 5:
            return min(S[index])
