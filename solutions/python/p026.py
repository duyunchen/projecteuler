"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

"""
Rather than do this brute-forceish way, some number theory came to the rescue

http://en.wikipedia.org/wiki/Full_reptend_prime

Basically we can take multiples of 10 modulus the number, then take the result
of that, multiply by 10 and modulus the number.  Repeat until you get 1.  The number
of repeats required is the cycle length of the unit reciprocal of the number.  

Mind blown?
"""
def run():
    N = 1000
    longest = 0
    best = 0
    
    for n in range(2,N):
        #optimization: don't need to check multiples of 2 or 5
        if n % 2 == 0 or n % 5 == 0:
            continue
        
        length = get_reciprocal_cycle_length(n)
        
        if length > longest:
            longest = length
            best = n
            
    return best

# Returns the reciprocal cycle of n
def get_reciprocal_cycle_length(n):
    count = 1
    rem = 10 % n
    while rem != 1:
        rem = (rem * 10) % n
        count += 1
    return count
