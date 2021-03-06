"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""


def run():
    """
    Since Python has more or less arbitrary length integers, we can just do
    this the brute force way and have no overflows and still pretty fast
    """
    for index, fib in enumerate(fibgen()):
        if len(str(fib)) >= 1000:
            return index + 1


# A fibonacci sequence generator
def fibgen():
    a = 0
    b = 1
    while True:
        if a is 0:
            yield 1
        c = a + b
        a = b
        b = c
        yield c
