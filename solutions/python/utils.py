import math

# Finds the GCD between two numbers
def gcd(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a % b)

# Computes the product of a list of numbers
def product(numbers):
    if len(numbers) is 0: return 0
    elif len(numbers) is 1: return numbers[0]
    return reduce(lambda x,y: x*y, numbers)
    
# Determines if a number is prime
def is_prime(num):
    if num == 2: return True #trival cases
    if num % 2 == 0: return False 
    
    n_sqrt = int(math.ceil(math.sqrt(num)))
    for x in xrange(3,n_sqrt + 1,2):
        if num % x == 0:
            return False
    return True

# Generator for permutations of a string
def generate_perm(string):
    if len(string) == 1:
        yield string
   
    for i in xrange(len(string)):
        for perm in generate_perm(string[:i] + string[i+1:]):
            yield string[i] + perm
            
# Returns whether all the elements in a list are equal
def all_equal(x):
    return x.count(x[0]) == len(x)

# Returns whether a list is sorted
def is_sorted(L):
    return all(L[i] <= L[i+1] for i in xrange(len(L)-1))

# Returns whether a list is reverse sorted
def is_reverse_sorted(L):
    return all(L[i] >= L[i+1] for i in xrange(len(L)-1))
    
# Returns the sum of the first n natural numbers
def get_sum_of_first_n(n):
    return n*(n+1)/2

# Returns a list of divisors of a number
def get_divisors(n, sort=True):
    if n <= 3: return [1,n]
    divisors = set()
    n_sqrt = int(math.ceil(math.sqrt(n)))
    for x in xrange(1,n_sqrt + 1):
        if x in divisors:
            continue
        if n % x == 0:
            divisors.add(x)
            if n/x != x: divisors.add(n/x)
    return sorted(list(divisors)) if sort else list(divisors)

# Returns a boolean list of size n. a[i] = True if i is prime, false otherwise
def get_prime_sieve(n):
    if n is 0:
        return []
    if n is 1:
        return [False]
    
    sieve = [True if i%2 else False for i in xrange(n+1)]
    
    index = 3
    limit = int(math.sqrt(n))
    while index <= limit:
        multiplier = 3
        m_index = index*multiplier
        
        while m_index <= n:
            sieve[m_index] = False
            multiplier += 2
            m_index = index*multiplier
            
        index += 2
    
    sieve[1] = False
    sieve[2] = True #special cases
    return sieve

def combination(a, b):
    top = a
    bottom = b if a - b < b else a - b
    return product(range(bottom+1, top+1))/factorial(top - bottom)
    
def factorial(n):
    return product(range(2,n + 1))
    
     