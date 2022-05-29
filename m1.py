"""
m1.py
"""

import random

import time
import math


def length_longest(lst):
    res=0
    hold=0
    """Returns the length of the longest (sub-)list in lst"""
    if type(lst)!=list:
        return 0
    else:
        for x in lst:
            res+=1
            if type(x)==list:
                hold=length_longest(x)
    return max(hold,res)



def bubbelsort(aList):
    for i in range(len(aList)-1):
        for j in range(len(aList)-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                

def foo(n):
    result = 1
    for k in range(3):
        for i in range(n*n):
            result += k*n
    return result
    

def main():
    print(length_longest(1))                   # Should be 0
    print(length_longest([]))                  # Should be 0
    print(length_longest([1,2,3]))             # Should be 3
    print(length_longest([1,[2,3]]))           # Should be 2
    print(length_longest([1,[1,2,3,4],3]))     # Should be 4 

    aList=[3,2,5,1,7]
    bubbelsort(aList)
    print(aList)

    Tlst=[]
    exlst=[10, 100, 1000, 10000]
    for i in exlst:
        tstart = time.perf_counter ()
        foo(i)
        tstop = time.perf_counter ()
        Tlst.append(tstop-tstart)
        print(f'n={i} time= {tstop-tstart}')
    print(Tlst)
    


if __name__ == "__main__":
    main()
    
"""
Solution to A2 (Time complexity for bubbelsort):

går igenom alla n-1 tal
går igenom alla n-1 tal
sen + 2*n == n^2 detta på grund av att man






Solution to B1 (Time complexity for function foo):
n=10 time= 1.4499993994832039e-05
n=100 time= 0.0012620000052265823
n=1000 time= 0.11687040000106208
n=10000 time= 12.627455800000462

looks like a c*x^n
time_100/time_10 =x^90 
time_1000/time_100=x^900 osv

x=1.050877
x=1.0050
x=1.0005

det borde göra att för sista är det 1.00005
vilket gör 3.489*10^19 sek, många år



fel det är n^2 så 1000 ger T_1000=c*n^2
32 timmar

går också att räkna 100^2*12.627

ger 35 timmar


"""
    