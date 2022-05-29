""" linked_list.py

Student: Winston Olsson
Mail: Winston.lidingo@hotmail.com
Reviewed by: Alicia Robertsson
Date reviewed: 06/05-2022
"""












from numpy import insert


class LinkedList:
    
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ      
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self): 
        lst=self.first
        n=0            # Optional
        while lst:
            lst=lst.succ
            n+=1
        return n
  
  
    def mean(self):               # Optional
        sum=0
        f=self.first
        while f:
            sum+=f.data
            f=f.succ
        return sum/self.length()

    
    
    def remove_last(self):        # Optional
        len=self.length()
        f=self.first
        if len==1:
            ans=f.data
            self.first=None
            return ans
        for i in range(len-2):
            f=f.succ
        a=f.succ
        f.succ=None
        
        return a.data #Om det inte finns en list letar man efter self.first=None, retunera No lst
    
    
    def remove(self, x):          # Compulsory
        if self.first.data==x:
            self.first=self.first.succ #Geni Winston, Gäller bara för första.
            return True
        else:
            f=self.first
            while f:
                a=f.succ
                if f.succ==None: #Ordning var viktig
                    print('slut på lst')
                    return False
                if a.data==x:
                    f.succ=f.succ.succ #BRAINPOWER!Nästa nod är egentligen näst nästa.
                    print(f'tal som togs bort {x}')
                    return True

                f=f.succ
                

    
    
    def count(self, x):           # Optional
        return( self._count(x, self.first))
    def _count(self, x, f):
        if f.succ==None:
            if f.data==x:
                return 1
            else:
                return 0
        else:
            if f.data==x:
                return 1+self._count(x,f.succ)
            else:
                return 0+self._count(x,f.succ)
    
    
    def to_list(self):            # Compulsory
        lst=[]
        if self.first==None:
            return lst
        else:
            self._to_list(self.first,lst)
            print(lst)
            return lst
    def _to_list(self,f,lst):
        if f.succ==None:
            return lst.append(f.data)
        else:
            lst.append(f.data)
            return self._to_list(f.succ,lst)

    
    
    def remove_all(self, x):      # Compulsory
        return(self._remove_all(self.first,x))

    def _remove_all(self,f,x):
        if f.data==x: #Fisxar starten
            self.first=f
            self.first=self.first.succ
        if f.succ==None: #FIxar slutet
            if f.data==x:
                self.first=f
                self.first=self.first.succ
        elif f.succ.data==x: 
            f.succ=f.succ.succ         
            return self._remove_all(f,x)
        else:
            f=f.succ
            return self._remove_all(f,x)
        
    
    
    def __str__(self):
        return f'({(self._str(self.first))}' #Vackert

    def _str(self,f):           #Blev lättare att skriva rekursivt om man skulle ta return då man inte kan ta return under en while'
        if self.first==None: #Ta hand om None
            return f')'
        elif f.succ==None:
            return f'{f.data})'
        else:
            return f'{f.data}, {self._str(f.succ)}'

    
    def merge(self, lst):         # Compulsory
        for i in lst:
            self.insert(i)
    #För varje nytt element måste jag gå igenom i bästa fall ett element i värsta fall alla så från n+1 till n^2
    
    
    def __getitem__(self, ind):   # Compulsory
        f=self.first #Nu tittade jag inte på internet med detta kändes otroligt logiskt
        count=0
        while f:
            if ind==count:
                return f.data
            else:
                f=f.succ
                count+=1 #räkna framm per itteration
        
        return 'Index utanför lista'


class Person:                     # Compulsory to complete, Denna borde egentligen vara insatt ??
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
       
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __le__(self,diff): #Dessa två valdes för de används i insert
        if self.name==diff.name:
            return self.pnr < diff.pnr #Om samma namn, sortera efter pnr
        return self.name < diff.name #Notera att stor bokstav spelar roll om man väljer namn

    def __gt__(self,diff):
        return self.name > diff.name



    

def main():
    lst = LinkedList()
    #for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7,9,9,8]:
        #lst.insert(x)
    #print(lst)
    pers=['John','William','Fredrik','Clas','Clas']
    pnr=[1234,8934,2333,9074,9111]
    for i in range(len(pers)):
        pst=Person(pers[i],pnr[i])
        lst.insert(pst)
        
    print(lst)


    
    
    
    # Test code:

    


if __name__ == '__main__':
    main()
    

