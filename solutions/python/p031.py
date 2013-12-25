"""
In England the currency is made up of pound, $, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).

It is possible to make $2 in the following way:

1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can $2 be made using any number of coins?
"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def run():
    """
    Solution: Use recursion to count the combinations
    """
    N = 200
    return num_of_ways(0, N)


def num_of_ways(pos, total):
    """
    Recursively find the combos by trying multiples of the lowest coins first
    from the pos-th coin to the last coin.
    """
    first = coins[pos]

    if pos == len(coins) - 1:
        return 0 if total % first else 1

    count = 0
    for i in xrange(total / first + 1):
        count += num_of_ways(pos + 1, total - i * first)

    return count
