#! /usr/bin/python

# function without return statement
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

# call fib function
print 'fib(2000)'
raw_input('press any to continue...')
fib(2000)
# assign fib to another name
f = fib
print '\nfib(0) = ?'
raw_input('press any to continue...')
print f(0)

# hold on
raw_input('press any to continue...')

# function return list
def fib2(n):
    """Return a list containing the Fibonacci up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b

    return result

# call fib2
print 'f100 = fib2(1000)'
raw_input('press any to continue...')
f100 = fib2(1000)
print f100
