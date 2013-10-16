"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

words = {
         1: "one", 
         2:"two", 
         3:"three", 
         4:"four", 
         5:"five", 
         6:"six", 
         7:"seven", 
         8:"eight", 
         9:"nine", 
         10:"ten",
         11:"eleven",
         12:"twelve",
         13:"thirteen",
         14:"fourteen",
         15:"fifteen",
         16:"sixteen",
         17:"seventeen",
         18:"eighteen",
         19:"nineteen",
         20:"twenty",
         30:"thirty",
         40:"forty",
         50:"fifty",
         60:"sixty",
         70:"seventy",
         80:"eighty",
         90:"ninety",
         100:"hundred",
         1000:"thousand"}

# Pretty interesting problem.  Just need a dictionary that maps from numbers to 
# words and reconstruct words from numbers.
def run():
    MAX = 1000
    result = ""
    debug = []
    for n in xrange(1, MAX + 1):
        word = convert(n)
        result += word
        debug.append(word)
        
    return len(result)

def convert(n):
    if n <= 0:
        return ""
    elif n <= 20:
        return words[n]
    elif n <= 99:
        ones = n % 10
        tens = n - ones
        return words[tens] + words[ones] if ones > 0 else words[tens]
    elif n <= 999:
        tens = n % 100
        hundreds = (n - tens)/100
        
        if tens == 0:
            return words[hundreds] + words[100]
        else:
            return words[hundreds] + words[100] + "and" + convert(tens)
    elif n == 1000:
        return words[1] + words[1000]
    