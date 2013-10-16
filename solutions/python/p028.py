"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Solution: We notice a pattern 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25
the gaps between the numbers are 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6... etc
"""
def run():
    N = 1001
    
    total = 0
    current = 1
    increment = 2
    counter = 0
    
    while current <= N*N:
        total += current
        current += increment
        counter += 1
        if counter == 4:
            counter = 0
            increment += 2 
    
    return total
