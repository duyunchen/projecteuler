"""
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 632382518061  519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math

# We just compare the logarithms instead of the full number
def run():
    numbers = read_numbers()
    
    largest = 0
    largest_pos = 0
    for index, pair in enumerate(numbers):
        n = pair[1] * math.log(pair[0])
        if n > largest:
            largest = n
            largest_pos = index + 1
    
    return largest_pos
    
def read_numbers():
    with open("data/p099 base_exp.txt") as f:
        return map(lambda pair: map(int, pair.split(",")), f.read().split("\n"))
        
