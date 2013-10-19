"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

from utils import alphabet, read_file

# Pretty easy.  Basically just follow the given rules.
def run():
    names = sorted(read_file("data/p022 names.txt"))
    
    total = 0
    for index, name in enumerate(names):
        pos = index + 1
        total += get_alphabetical_value(name) * pos
        
    return total
        
def get_alphabetical_value(word):
    return sum([alphabet[c] for c in word.lower()])
    


