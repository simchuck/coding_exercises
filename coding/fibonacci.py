#FibonacciSeries = [0, 1]
#FibonacciSeries = [FibonacciSeries[i] + Fibnoacci[i - 1] for i in range(1, 50)]
#i + j for i in range(50)]



def fib_memo(n, memo=[]):
    """
    Return values from Fibonacci Series using dynamic programming algorithm.
    """

    if n == 0:
        fibonacci = 0
    elif n == 1:
        fibonacci = 1

    try:
        return memo[n]
    except:
        memo[n] = fib_memo(n-2, memo) + fib_memo(n-2, memo)
        return memo[n]

    # this solution would be constant order on time, but the space
    # complexity grows as we accumulate more values in the memoization state

    ### also, I have an error in above...


if __name__ == '__main__':

    fibonacci_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    memo = []

    for n, expected in enumerate(fibonacci_series):
        print('fib({0}) = {1}'.format(n, expected))
        assert fib_memo(n, memo) == expected

#def fib_naive(n):
#    if n == 0: return 0
#    if n == 1: return 1
#    for i in range(2, n+1):
#        result +=

# this one works
def fib_recursive(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)


### NOT TESTED
#def fib_dynamic(n, memo):
#    memo = [0, 1]
#    if n < len(memo): return memo[n]
#    memo[n] =
#    if n > len(memo): memo[n] = memo[n-1] + memo[n-2]
#    return memo[n]



def fib_minspace(n):
    a = 0
    b = 1
    if n < 1: print('Invalid')
    elif n == 0: return a
    elif n == 1: return b

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c
    # problem with this is that it has to run through the for loop each time
    # good on overall space, but linear on time

def test_fib_0():
    expected = 0
    result = fib_minspace(0)
    assert result == expected
    result = fib_recursive(0)
    assert result == expected
    result = fib_dynamic(0)
    assert result == expected
