"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""

import time # to compute runtimes
from tqdm import tqdm # progress bar
from egyptian import isodd # haven't taught students about imports yet
import numpy as np # need this for power version
import matplotlib.pyplot as plt

# Question 2
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

if __name__ == '__main__':
    for n in range(30):
        print(fibonacci_recursive(n))


# Question 2
def fibonacci_iter(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    for n in range(30):
        print(fibonacci_iter(n))

# Question 3
def fibonacci_power(n):
    if n == 0:
        return 0

    def power(A, n):
        if n == 0:
            return np.eye(2) # multiplicative identity
        if n == 1:
            return A

        if isodd(n):
            return power(A @ A, n // 2) @ A
        else:
            return power(A @ A, n // 2)

    A = np.array([[1,1],[1,0]])
    b = np.array([1,0])

    An = power(A, n-1)
    x = An @ b
    return x[0]

if __name__ == '__main__':
    for n in range(30):
        print(fibonacci_power(n))


if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts


    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    ## write your code for problem 4 below...
    plt.loglog(nrecursive, trecursive, label='recursive')
    plt.loglog(niter, titer, label='iter')
    plt.loglog(npower, tpower, label='power')
    plt.xlabel('n')
    plt.ylabel('time (sec.)')
    plt.title('time to compute fibonacci(n)')
    plt.legend()
    plt.savefig('fibonacci_runtime.png')
