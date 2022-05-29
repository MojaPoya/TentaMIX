"""
Solutions to exam tasks for module 3.
Name:
Code:

The file contains:
   1) the class LinkedList with tasks A5, A6 and B2,
   2) the class BST with tasks A7, A8, 
   3) the function bst_sort to be analyzed in task B3
 

The main function runs a small test of the methods. Note that main will not
fully function until all tasks are solved.
"""
import random
import time
import math


class ExamException(Exception):
    def __init__(self, arg):
        self.arg = arg


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def add_last(self, x):
        """ Adds x at the end of the list """
        if self.first == None:
            self.first = self.Node(x)
        else:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = self.Node(x)

    def remove_all(self, x):
        """ Removes all ocurrencies of x in the list """
        self.first = self._remove_all(x, self.first)

        

    def _remove_all(self, x, f):
        if f.data==x:
            self.first=self.first.succ
        if f.succ==None:
            return self.first
        if f.succ.data==x:
            f.succ=f.succ.succ #Ta bort
            return self._remove_all(x,f)
        else: 
            return self._remove_all(x,f.succ) #stega

        """ Task A5:
            Remove all x from list starting with node f.
            Return the first node in the remaing list.
        """
        pass


    def length(self):
        lst=0
        if self.first==None:
            return 0
        f=self.first
        while f.succ:
            f=f.succ
            lst+=1
        lst-=1
        return lst

    def insert(self, data, index=0):
        if index<(self.length()-1):
            return 'INDEX OUT' 
        count=0
        if index==count:
            self.first=self.Node(data,self.first)
        else:
            f=self.first
            while f.succ and count<index-1:
                f=f.succ
                count+=1
            f.succ=self.Node(data,f.succ)
    

        """ B2: Inserts a new node at a specified index """
        


####################################


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.data
            if self.right:
                yield from self.right

        def __str__(self):
            return str(self.data)


    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.add(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ' '
        return '<' + result + '>'

    def add(self, x):
        """ Adds a new node to the tree"""
        def _add(x, r):
            if r == None:
                return self.Node(x)
            elif x < r.data:
                r.left = _add(x, r.left)
            elif x > r.data:
                r.right = _add(x, r.right)
            return r
        self.root = _add(x, self.root)

    def count_leaves(self):
        """ Returns the number of leaves """
        return self._count_leaves(self.root)

    def _count_leaves(self, r):
        if r.right==None and r.left==None:
            return 1
        elif r.right==None:
            return 0+self._count_leaves(r.left)
        elif r.left==None:
            return 0+self._count_leaves(r.right)
        else:
            return 0+self._count_leaves(r.right)+self._count_leaves(r.left)
        """ A7:
            Count the leaves in the subtree with root r
        """
    def __eq__(self,diff):
        return str(self)==str(diff) #Mycket bra att kunna
    
 


def bst_sort(aList):
    """ Returns a sorted list"""
    bst = BST()
    for x in aList:
        bst.add(x)
    result = []
    for x in bst:
        result.append(x)
    return result


def main():
    print('\nTest run of m3.py')

    print('\nTest of A5 (remove_all)')
    lst = LinkedList()
    for x in (3, 1, 2, 3, 4, 3, 4, 7, 3):
        lst.add_last(x)
    print(lst)

    lst.remove_all(3)
    print(lst, ' \t Should be (1, 2, 4, 4, 7)')

    print('\nTest of B2 (insertion at an index)')
    lst = LinkedList()
    lst.insert(3)          # <3>
    lst.insert(5, 1)       # <3, 5>
    lst.insert(5)          # <5, 3, 5>
    lst.insert(4,1)       # <5, 4, 3, 5>
    print(lst, ' \t Should be (5, 4, 3, 5)')
    try:
        lst.insert(1, 99)      # LinkedListError: Index out range: 99
    except ExamException as e:
        print(e)

    print('\nTest of A7: Number of leaves')
    bst = BST([5, 2, 1, 3, 6, 4])
    print('Number of leaves:', bst.count_leaves(), ' \t Should be 3')

    print("\nTest of A8: == for BST")
    print(BST() == BST(), ' \t Should be True')
    print(BST([1, 2, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([2, 1, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([0, 1, 3]) == BST([1, 2, 3]), ' \t Should be False')
    print(BST([1, 2, 3]) == BST([1, 2]), ' \t Should be False')

    print('\nDemonstration of bst_sort')
    print(bst_sort([5, 2, 4, 8, 1, 9, 3]))


if __name__ == '__main__':
    main()

"""\n\nAnswer to task A6 - Complexity of repeated add_last:
theta(n) dvs n lång tid eller c*n lång tid. Om ett sätta in ett värde tar
c lång tid dvs en opperation. måste vi för att sätta in ett tal längst bak i en lista
göra n steg för att kommma dit, detta gäller vid placering av ett tal.

för att köra hela koden krävs n stycken opperationer, om varje tal tar n blir det ungefär
c*n^2  c(0,1,2,3,4,5,n-1)= n stycken opperationer 

    """

"""\n\nAnswer to task B3 - Complexity of bst_sort:
Vi tänker realistiskt, först tar vi och lägger in saker i en lista, då den är sorterad
kan vi med list tilllägning i bästa fall få n-1 och värsta fall n^2, värsta fall
är som föregående uppgift, lägnst bak varje gång, bästa vall är lägnst fram
sen multiplicera detta med n för att lägga in allt i listan ==n^3


    """
