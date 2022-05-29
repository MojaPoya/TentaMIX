#Ma4 Winston Olsson
#Mail:
#Datum
#Redovisad för:

from time import perf_counter as pc
from time import sleep as pause
#import multiprocessing as mp
import concurrent.futures as future

import functools

import matplotlib.pyplot as plt
import random
import math
PIexact=math.pi
def simple_sphere():

    lst=[100, 1000, 10000, 100000]
    expPI=[]
    xlst=[]
    ylst=[]
    figi=1

    xb=[]
    yb=[]

    for n in lst:
        n_c=0
        fig, ax = plt.subplots()
        for i in range(n):
            x=random.uniform(-1,1) #Halvöppet intervall, ger bättre uppskatting vid öppet
            y=random.uniform(-1,1)
            if (x**2)+(y**2)<=1:
                n_c+=1
                xlst.append(x)
                ylst.append(y)
            else:
                xb.append(x)
                yb.append(y)


        ax.scatter(xb,yb,c='blue')
        ax.scatter(xlst,ylst,c='red')
        print(f'PI= {PIexact}, approximerat PI= {4*n_c/n} för {n} antal punkter')
        plt.figure(figi)
        
        plt.savefig(f'PIaprox, n= {n}.png')
        figi+=1
        expPI.append(4*n_c/n)
    return 'Done'





###################
def coolsphere(d,n):
    real= lambda d : (math.pi**(d/2))/(math.gamma((d/2)+1))
    f=functools.reduce(lambda x,y : x+y,[1 for j in range(n) if sum([(random.uniform(-1,1))**2 for i in range(d)])<=1])*(2**d)/n
    return f , real(d)

#################


def runner(n):
    print(f"Performing a costly function {n}")
    print(f"Function {n} complete")


if __name__ == "__main__":
    multi=False
    start = pc()
    # p1 = mp.Process(target=runner)
    # p2 = mp.Process(target=runner)
    # processes = []
    # for _ in range(10):
    #     p = mp.Process(target=some_method, args=[some_var])
    #     processes.append(p)
    # for p in processes:
    #     p.start()
    # for p in processes:
    #     p.join()
    if multi==True:
        pro=[]
        with future.ProcessPoolExecutor() as ex:
            for _ in range(10):
                p = ex.submit(coolsphere, 11,1000000) 
                pro.append(p)
            for i in range (10):
                r=pro[i].result()
    else:
        coolsphere(11,10000000)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

#Process took 14.61 seconds 10 proc
#Process took 78.12 seconds 1 proc
