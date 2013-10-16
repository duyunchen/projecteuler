"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Pretty straight forward. We just follow the definition.
def run():
    MAX = 1000000
    
    # optimization: we use this to cache values that already have been computed
    cache = {}
    
    largest = 0
    largest_number = 0
    for i in xrange(MAX):
        depth = cache[i] if cache.get(i) else run_collatz(i, cache)
        if depth > largest:
            largest = depth
            largest_number = i
    return largest_number
    
def run_collatz(n, cache):
    if n <= 1:
        cache[n] = 1
        return 1
    else:
        if n % 2 == 0:
            if not cache.get(n/2):
                cache[n/2] = run_collatz(n/2, cache) + 1
            return cache[n/2]
        else:
            if not cache.get(3*n + 1):
                cache[3*n + 1] = run_collatz(3*n + 1, cache) + 1 
            return cache[3*n + 1]
        
        
        
    