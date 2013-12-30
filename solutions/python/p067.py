"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)
"""
from utils import read_file


def run():
    """
    I already solved this with the efficient method in problem 18 so I'm
    just going to copy that code over.
    """
    triangle = [map(int, line.split(' ')) for line in \
                read_file('data/p067 triangle.txt', line_delim='\n') if line]

    height = len(triangle)

    for index in xrange(height - 2, -1, -1):
        row = triangle[index]
        next_row = triangle[index + 1]
        for i in xrange(len(row)):
            row[i] += max(next_row[i], next_row[i + 1])

    return triangle[0][0]
