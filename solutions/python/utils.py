import math

alphabet = { char : index+1 for index,char in enumerate("abcdefghijklmnopqrstuvwxyz")}

# Reads a text file in the standard EP format
def read_file(filename):
    with open(filename) as f:
        return map(lambda x: x.replace('"', '').strip(), f.read().split(","))

# Determines if a number is a perfect square
def is_square(n):
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
    
# Finds the lcm between two numbers
def lcm(a, b):
    return a*b/gcd(a,b)
    
# Finds the LCM between two numbers
def gcd(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a % b)

# Returns whether x is a palindrome
def is_palindrome(x):
    return str(x) == str(x)[::-1]

# Converts a number to string binary
def to_binary(n):
    if n==0: return ""
    else:
        return to_binary(n/2) + str(n%2)
    
# Computes the product of a list of numbers
def product(numbers):
    if len(numbers) is 0: return 0
    elif len(numbers) is 1: return numbers[0]
    return reduce(lambda x,y: x*y, numbers)
    
# Determines if a number is prime
def is_prime(num):
    if num == 2: return True
    if num == 1 or num % 2 == 0: return False 
    
    n_sqrt = int(math.ceil(math.sqrt(num)))
    for x in xrange(3,n_sqrt + 1,2):
        if num % x == 0: return False
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

# Returns unique primes factors of a number
def get_prime_factors(n):
    factors = set()
    sieve = get_prime_sieve(n//2 + 1)
    for i in xrange(2, len(sieve)):
        if sieve[i] and n % i == 0:
            factors.add(i)
            n /= i
        while sieve[i] and n % i == 0:
            n /= i
    return factors
    
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
            divisors.add(n/x)
    return sorted(list(divisors)) if sort else divisors

# Generator for rotations of string s 
def generate_rotation(s):
    if len(s) == 0:
        yield None
    elif len(s) == 1:
        yield s[0]
    else:
        for _ in xrange(len(s)):
            s = s[1:] + s[0]
            yield s

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

# Returns a choose b
def combination(a, b):
    top = a
    bottom = b if a - b < b else a - b
    return product(range(bottom+1, top+1))/factorial(top - bottom)

# Returns n!
def factorial(n):
    if n <= 1: return 1
    return product(range(2,n + 1))

# A counter class that holds key -> count pairs
class Counter():
    def __init__(self):
        self.counter = {}
    
    def add(self, obj):
        if not self.counter.get(obj):
            self.counter[obj] = 1
        else:
            self.counter[obj] += 1
            
    def get(self, obj):
        if not self.counter.get(obj):
            return 0
        else:
            return self.counter[obj]
    
    # returns item with the highest count along with the count
    def get_most(self):
        largest = -1
        best = None
        for key, value in self.counter.items():
            if value > largest:
                largest = value
                best = key
        return best, largest