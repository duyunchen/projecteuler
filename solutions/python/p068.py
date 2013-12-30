"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set: 4,3,2;
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

Total    Solution Set
9    4,2,3; 5,3,1; 6,1,2
9    4,3,2; 6,2,1; 5,1,3
10    2,3,5; 4,5,1; 6,1,3
10    2,5,3; 6,3,1; 4,1,5
11    1,4,6; 3,6,2; 5,2,4
11    1,6,4; 5,4,2; 3,2,6
12    1,5,6; 2,6,4; 3,4,5
12    1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16- and 17-digit strings. What is the maximum 16-digit string for a
"magic" 5-gon ring?
"""
from itertools import combinations, permutations
from utils import generate_rotation


def run():
    """
    Brute force with some optimizations.

    Since we are looking for a 16-digit string, the 10 must be an outside node.
    """
    digits = range(1, 11)

    strings = []
    for inner_set in combinations('123456789', 5):
        for inner in permutations(inner_set):
            inner = map(int, inner)
            outer = set([n for n in digits if n not in inner])
            total = (sum(inner) * 2 + sum(outer))
            if total % 5 > 0:
                continue
            total /= 5
            inner, lines = inner + [inner[0]], []
            for i in xrange(5):
                s = inner[i: i + 2]
                n = total - sum(s)
                if n in outer:
                    lines.append([n] + s)
                    outer.remove(n)
                else:
                    break
            else:
                sorted_lines = sorted(lines)
                for rotation in generate_rotation(lines):
                    if rotation[0] == sorted_lines[0]:
                        break
                strings.append(int(''.join([str(n) for line in rotation \
                                        for n in line])))

    return max(strings)
