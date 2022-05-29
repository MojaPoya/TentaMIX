"""
Solutions to exam tasks for module M4
Name:
Code:
"""
import concurrent.futures as future

import functools
# A9
def get_balance(index):
    """This method opens customers.json and returns the field
    'balance' for the person with the given index.
    Leave this method as is.
    Note that '$' and ',' are removed from 'balance' in the jason file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))

def get_total_balance():
    """Method that runs get_balance in parallel for each index 0-111.
    The method should return the sum of all balances."""
    tb=0
    pro=[]
    indexes=range(112)
    import concurrent.futures as future
    with future.ThreadPoolExecutor(10) as ex:
        balances = functools.reduce(lambda x,y:x+y,list(ex.map(get_balance, indexes)))
    return balances
    for i in range(112):
         tb=tb+get_balance(i)
    return tb ,r
    
# A10

def get_mean_balances():
    """Method that return the mean balance for male and female customes. Gender 
    is set in the field 'gender' ('male' or 'female')"""
    import json
    mlst=[]
    flst=[]
    with open('customers.json') as f:
        data = json.load(f)
        for i in range(112):
            if str(data[i]['gender'])=="female":
                flst.append(get_balance(i))
            else:
                mlst.append(get_balance(i))
    fmb=sum(flst)/len(flst)
    mmb=sum(mlst)/len(mlst)
    return fmb ,mmb
      
    
# B4
def leapyears(years):
    """A method the returns the leap years of the years in the in argument years"""
    leap=[i for i in years if i%4==0  and i%100!=0 or i%400==0 ]
    return leap


def main():
    print('Test of A9 ')
    print(get_total_balance())
    print('Test of A10 ')
    print(get_mean_balances())
    print('Test of B4 ')
    ly=leapyears(range(1900,2101))
    print(ly)
    if ly != None:
        print(len(ly))

if __name__ == "__main__":
    main()
    print('Over and out')
