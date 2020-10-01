"""
Egyptian algorithm
"""

def isodd(n):
    """
    returns True if n is odd
    """
    return n & 0x1 == 1

def egyptian_multiplication(a, n):
    """
    returns the product a * n

    assume n is a positive integer
    """

    if n == 1:
        return a
    if n == 0:
        return 0

    if isodd(n):
        return egyptian_multiplication(a + a, n // 2) + a
    else:
        return egyptian_multiplication(a + a, n // 2)


if __name__ == '__main__':
    # this code runs when executed as a script
    for a in [1,2,3]:
        for n in [1,2,5,10]:
            print("{} * {} = {}".format(a, n, egyptian_multiplication(a,n)))


# all you need to do is copy and paste the above function, change the name for recursion
# and change additions to multiplications
# also need to modify the case for n == 0 to be the mutliplicative identity instead of additive identity
def power(a, n):
    """
    computes the power a ** n

    assume n is a positive integer
    """

    if n == 1:
        return a
    if n == 0:
        return 1 # multiplicative identity

    if isodd(n):
        return power(a * a, n // 2) * a
    else:
        return power(a * a, n // 2)
