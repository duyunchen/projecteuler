"""
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from utils import alphabet, read_file, is_square

"""
Solution: We observe that since a triangle number is given by x = n(n+1)/2, 
8*x + 1 = 4n(n+1) + 1 = 4n^2 + 4n + 1 = (2n + 1)^2 which is a perfect square.

So to test for whether a number is a triangle number, we test if 8x + 1 is a 
perfect square.
"""
def run():
    words = read_file("data/p042 words.txt")
    
    count = 0
    for word in words:
        
        n = sum(map(lambda s: alphabet[s], word.lower()))
        
        if is_square(8*n + 1):
            count += 1
    
    return count
        