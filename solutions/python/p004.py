"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#Solution: just a double loop through all 3-digit numbers and check
#if the product is palindrome while keeping track of the largest.
def run():
    largest = 0
    for a in xrange(100,1000):
        for b in xrange(100,1000):
            p = a * b
            if is_palindrome(p) and p > largest:
                largest = p
    return largest

#Check if a number is a palindrome by reversing the number
def is_palindrome(num):
    return str(num) == str(num)[::-1]