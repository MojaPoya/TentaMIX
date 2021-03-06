""" bst.py

Student: Winston Olsson
Mail: winston.lidingo@hotmail.com
Reviewed by: Alicia Robertsson
Date reviewed: 06/05-2022
"""


import random
import math


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)
    def _height(self,r):
        if r is None:
            return 0
        else:
            right=self._height(r.right)
            left=self._height(r.left)
        return 1+ max(right,left)  #Tittar varje g??ng vilken sida som ??r st??rts, dvs en ger ju en ettta och en ger en nolla.. Rekusivt t??nkande.
                
            

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):
                   # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k) #H??r gick jag lite p?? k??nsla och verkar funka. Insperation fr??n insert funktionen
        elif k > r.key:
            r.right =  self._remove(r.right,k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.            # Find the smallest key in the right subtree
                a=r.right #g?? h??ger f??rst
                while a.left!=None:            # Put that key in this node
                    a=a.left #man g??r s?? l??gnt v??nster man kan        # Remove that key from the right subtree
                r.key=a.key #Tog v??ldig tl??ng tid innan jag kom hit, r??kade alltid to bort noden efter men nu f??rst??r jag??
                #Jag f??rs??kte byta ut noderna men ist??llet nu bytte jag bara ut nycklarna n??r jag hittat den l??gsta
                r.right=self._remove(r.right,a.key) #Sist s??ger vi nu att vi tar bort fr??n det h??gra tr??det v??ran nod vi la in
                #Vi g??r h??ger f??r att om vi bytt ut starten har vi ju nu tv?? noder av samma namn, d?? tar vi bort den som ??r i tr??dets h??gra
                #Halva som fortfarande ??r kvar.
                

        return r  # Remember this! It applies to some of the cases above

    def __str__(self):
                  # Compulsory
        return f'<{(self._str(self.root))}>' 


    def _str(self,r): #Kankse lite mycket harcoding
        if r==None:
            return '' 
        elif r.right==None and r.left==None:
            return r.key
        elif r.right==None:
            return f'{self._str(r.left)}, {r.key}'
        elif r.left==None:
            return f'{r.key}, {self._str(r.right)}'
        else:
            return f'{self._str(r.left)}, {r.key}, {self._str(r.right)}'








    def to_list(self):            # Compulsory
        lst=[]
        if self.root==None:
            return lst
        else:
            self._to_list(self.root,lst)
            lst.sort()
            print(lst)
            return lst

    def _to_list(self,f,lst):
        if f==None:
            return lst
        if f.right==None and f.left==None:
            return lst.append(f.key)
        else:
            lst.append(f.key)
            return self._to_list(f.left,lst), self._to_list(f.right,lst)

    def to_LinkedList(self):                      # Compulsory Borde vara n^2 pga att den f??rst h??mtar samtliga nycklar, sen insertar den vilket ger f??reg??ende kostnad 
        lst=self.to_list()
        Linked=LinkedList()
        for n in lst:
            Linked.insert(n)
        return Linked


    def ipl(self):
        n=0  
        return(self._ipl(self.root,n))

    def _ipl(self,r,n):
        n+=1
        if r==None:
            return 0
        # elif r.right==None and r.left==None:
        #     return n
        # elif r.right==None:
        #     return n+self._ipl(r.left,n)
        # elif r.left==None:
        #     return n+self._ipl(r.right,n)
        else:
            return n + self._ipl(r.right,n)+self._ipl(r.left,n)


def random_tree(n):                               # Useful
    t=BST()
    for i in range(n):
        x=random.random()
        t.insert(x)
    return t


    




def main():
    # t = BST()
    # for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
    #     t.insert(x)
    # random_tree(5)
  

    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")
   
   
    lst=[1,10,10**2,10**3,10**4,10**5,10**6]
    lst2=[1,10,10**2,20**2,40**2,80**2,10**3,20**3,60**3,10**4,20**4,80**4,10**5]
    snittslst=[]
    explst=[]
    hojdlst=[]
    sizelist=[]
    for n in lst:
        RT=random_tree(n)
        snitt=RT.ipl()/RT.size()
        funk=1.39*math.log2(n)
        hojd=RT.height()
        snittslst.append(snitt)
        explst.append(funk)
        hojdlst.append(hojd)
        sizelist.append(RT.size())

    print(snittslst)
    
    print(explst)

    print(hojdlst)

    print(sizelist)
   
   
    #[1.0, 3.3, 9.41, 13.62, 15.88, 22.14985, 25.854044] verkligt snitt
    #[0.0, 4.617480051893433, 9.234960103786866, 13.8524401556803, 18.469920207573733, 23.087400259467167, 27.7048803113606] funktion
    #[1, 6, 18, 22, 28, 42, 48] h??jd
    #Hljden v??xer dubbelt sp snabbt

    #Detta ??r f??r lite fler v??rden och lst2



if __name__ == "__main__":
    main()


"""
What is the generator good for? F??rst??r inte helt vad som menas med givna tr??dgeneratorn, om om det ??r f??r att ber??kna l??gnd s?? f??lj svaren nedan.
==============================

1. computing size? Ja, den k??r ju p?? alla
2. computing height? Nej
3. contains? Ja
4. insert? Nej
5. remove? Nej


Om den menas vad ??r bra flr saker som man kan anv??nda den funkar ju alla metoder. ??r bara att s??tta RT.xxx

Results for ipl of random trees
===============================


[1.0, 3.7, 8.67, 10.22, 12.94875, 16.6759375, 11.363, 16.3165, 22.576300925925924, 16.9234, 21.77110625, 33.341708569335935, 22.34928]
[0.0, 4.617480051893433, 9.234960103786866, 12.014960103786867, 14.794960103786867, 17.574960103786868, 13.8524401556803, 18.0224401556803, 24.63173378368752, 18.469920207573733, 24.029920207573735, 35.149920207573736, 23.087400259467167]

detta var f??r lst2 tog 10 min att k??ra, ser ??nd?? lika ut, det ??r ett klart m??nster att de f??ljer varandra, det ??r d??remot ett m??nster att metoden hittar lite snabbare fram ??n vad som f??rv??ntas

"""
