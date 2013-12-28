"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""

from utils import Counter, get_prime_sieve, replacenth, powerset


def run():
    """
    Brute force over all the primes, retroactively incrementing family member
    count of all related numbers.  Using a estimated upper bound of a million.
    """
    N = 10 ** 6
    primes = get_prime_sieve(N)
    counter = Counter(track_max=True)
    powersets = [list(powerset(range(1, n + 1))) for n in range(6)]

    pattern = None
    for p, is_prime in enumerate(primes):
        if not is_prime or p < 10:
            continue

        s = str(p)

        # lol
        if '0' not in s and '1' not in s:
            continue

        for digit in '0123456789':
            # No need to replace the last digit due to parity
            num_appear = s[:-1].count(digit)
            if num_appear == 0:
                continue
            replace_positions = powersets[num_appear]

            for positions in replace_positions:
                if len(positions) == 0:
                    continue
                replaced = s
                for index, position in enumerate(positions):
                    replaced = replacenth(replaced, digit, '*',
                                          position - index)
                counter.add(replaced)
                if counter.get_most()[1] == 8:
                    pattern = counter.get_most()[0]

    # replace all the *'s with the lowest possible digit and return
    replace_digit = '1' if pattern[0] == '*' else '0'
    return int(pattern.replace('*', replace_digit))
