"""
Solutions to exam tasks for module 4.
"""

import concurrent.futures as future

import os
from PIL import Image
# A9
def matrix(x,n):
    """Method that returns a list of lists (with contents of each row of M),
    using a list comprehension"""
    lst=[[i**j for j in range(n) ] for i in x]
    return lst

# A10
def dice(n):
	"""Method thats simulates a broken dice. Do not modify."""
	from random import choice
	return [choice([1,2,3,4,5,5]) for _ in range(n)]

def dice_average():

    pro=[]
    with future.ProcessPoolExecutor() as ex:
        for _ in range(20):
            p = ex.submit(dice, 100000) 
            pro.append(p)
        for i in range (10):
            r=pro[i].result()
    return sum(r)/len(r)
 # remove and write your code here

# B4
def thumbnail():
    if os.path.isdir('thumb')==True:
        print('hej')
        lst=[]
        form=['.jpg','.png']
        names=[]
        currentd=os.getcwd()
        
        for i in os.listdir(currentd):
            for x in form:
                if x in i: 
                    names.append(i)
                    bild=Image.open(i)
                    bild=bild.resize((100,100))
                    lst.append(bild)
                    
       
        for i in range(len(lst)):
            lst[i].save('thumb/thumb_'+names[i])
    

    else:
        os.makedirs('thumb')
        return thumbnail()

#-------------------------------
def main():
    print('Test of A9 ')
    x=[5, 1.5, 3]
    print(matrix(x,3))
    print(matrix(x,4))
    print('Test of A10 ')
    print(dice_average())
    print('Test of B4 ')
    thumbnail()

if __name__ == "__main__":
    main()