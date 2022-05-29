"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count all occurencies of d recursively """
    if lst==[]:
        return 0
    if type(lst[0])==list:
        return count_all(lst[0],d)+count_all(lst[1:],d)
    elif lst[0]==d:
        return 1+count_all(lst[1:],d)
    else:
        return 0+count_all(lst[1:],d)


def c(n): #3 ger e1 sub, 4 ger 2 sub, 5 ger 3 sub, 6 
    if n <= 2:
        return 1
    else:
        return c(n-1) - c(n-3)


def c_mem(n):
    memory = {3:0, 4:-1} #Man kan lösa detta på ett snyggt sätt, om n är mindre än två änvänds ju inte dessa värden: man kan ockå starta lexikonnet på 0
    def c_memo(n):
        if n<=2:
            return 1
        elif n not in memory:
            memory[n] = c_memo(n-1) - c_memo(n-3)
        return memory[n]
    return c_memo(n)

    """ A2:
        Compute c(n) recursively as above but use
        memorization to keep the runtime down.
    """



def main():
    print('Test count_all')
    print(count_all([], 1))
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))

    print('\nTest of c')
    print('c(3):', c(3))
    print('c(4):', c(4))
    print('c(5):', c(5))
    print('c(9):', c(9))
    tstart = time.perf_counter ()
    c(45)
    tstop = time.perf_counter ()
    print(f"Measured time: {tstop -tstart} seconds")
    print('\nTest of c_mem')
    print('c_mem(3):', c_mem(3))
    print('c_mem(4):', c_mem(4))
    print('c_mem(5):', c_mem(5))
    print('c_mem(9):', c_mem(9))

    print('c_mem(100):', c_mem(100))

    print('\nCode for task B1')


if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:


419020678

"""
