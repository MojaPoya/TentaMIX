"""
Solutions to exam tasks for module 3.

The file contains the classes:
   1) LinkedList with tasks A5, A6 and A7
   2) BST with tasks  A8 and B3
   3) ExamException for handling exceptions 

Note:
   1. There are two implementation of the __init__ file in LinkedList.
      It is the last one that is used - it overrides the first one.
      The first on does not work until the method append is implemented.
   2. There is an exit statement in main preventing the timing code for
      assigmnet B3 to be run. Remove that statement when you start to work with B3.
   
"""
from lib2to3.pytree import Node
import random
import time

from sklearn import tree

class ExamException(Exception):            
    def __init__(self, msg):
        self.msg = msg


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ
            
    # This *second* implementation of __init__ has to be put in front of the
    # the first since id does not work until append is implemented.
    def __init__(self, param=None):            ### Second implementation  A7
        self.first = None
        if param is None:
            return
        try:
            iter(param)
        except TypeError:
            self.first = self.Node(param)
            return
        
        # Create the list from an iterable
        # Does not work before append is implemented
        for x in param:
            self.append(x)

    def __init__(self, param=None):            ### First implementation  A7
        self.first = None
        if param is None:
            return
        try:
            iter(param)
        except TypeError:
            self.first = self.Node(param)  
            return
        
        # Create the list from an iterable
        self.first = self.Node(None) # A dummy node
        temp = self.first
        for x in param:
            temp.succ = self.Node(x)
            temp = temp.succ
        self.first = self.first.succ # Remove thge dummy node

    
    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ
    
    def __str__(self):
        if self.first is None:
            return '()'
        res = ''
        for x in self:
            res += str(x) + ', '
        return '(' + res[:-2] + ')'
    
    def __getitem__(self, index):
        ind = 0
        for x in self:
            if ind == index:
                return x
            ind += 1
        raise ExamException(f'Index out of range: {index}')
    
    def __setitem__(self, index, value):                 ##### A6
        """ Store value at position index.
            ExamException if index < 0 or index >= n where n
            is the length of the list.
        """
        f=self.first
        count=0
        while f:
            if count == index:
                f.data=value
                return f
            f=f.succ
            count+=1
        raise ExamException(f'Index out of range: {index}')

        

    
    def append(self, x):
        """ Append a new element x at the end of the list"""

        self.first = self._append(self.first, x)
    
    def _append(self, f, x):  
                                 ##### A5
        if f==None:
            return self.Node(x)
        else:
            f.succ=self._append(f.succ,x)
            return f
    
class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, param=None):
        self.root = None
        if param:
            for x in param:
                self.insert(x)

    def __iter__(self):
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

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ', '
        if self.root:
            result = result[:-2]
        return '<' + result + '>'

        
    def ipl(self):
        return self._ipl(self.root, 1)

    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return level + \
                self._ipl(r.left, level + 1) + \
                self._ipl(r.right, level + 1)
    
    def is_omorph(self, other_tree):                             #### A8
        """ Returns True if self and other_tree has exactly the
            same structure, regerdless of the key values.
        """
        if self.ipl()==other_tree.ipl():
            return True
        else:
            return False

            
    def merge(self, other_bst):                                   #### B3
        """Inserts all keys from other_bst int this tree
        """
        for x in other_bst:
            self.insert(x)
    def to_list(self):
        lst=[]
        for i in self:
            lst.append(i)
        return lst

def better_merge(t1,t2): #LÖST
    t3=BST()
    Ts=t1+t2
    random.shuffle(Ts)
    for i in Ts:
        t3.insert(i)
    return t3

            

def random_tree(n):
    t = BST()
    for x in range(n):
        t.insert(random.random())
    return t
        

def main():
    print('Using append')
    print('============')
    ll = LinkedList()
    for i in range(5):
        print(i)
        ll.append(i)
    print('After som appends    : ', ll)
    ll.append('x')
    print('After one more append: ', ll)
    
    print('\nUsing index operations:')
    print('=======================')
    ll = LinkedList([2, 5, 8])
    print(ll)
    print(f'll[2]: {ll[2]}')
    try:
        ll[0] = 9
        ll[2] = 11
        print(ll)
        ll[-1] = 17
    except ExamException as e:
        print(e)
        

    print('\nTrying is_omorph')
    print('================')
    t1 = BST([1,2,3])
    t2 = BST([2,1,3])
    t3 = BST([2,3,1])
    t4 = BST([7,8,9])

    print(t1.ipl())
    print(t2.ipl())
    print(t3.ipl())
    print(t4.ipl())
    
    print(f't1 and t2: {t1.is_omorph(t2)}')
    print(f't1 and t3: {t1.is_omorph(t3)}')
    print(f't2 and t3: {t2.is_omorph(t3)}')
    print(f't1 and t4: {t1.is_omorph(t4)}')
    
    print('\n\nTime measuring for merge')
    print('========================\n')
    
    ################################
                            # Remove this line when working with B3
    ################################
    
    print('           Average node height')
    print('     n   t1     t2     t3     t4')
    m = 10

    for n in (1000, 2000, 4000, 8000, 16000,
              32000, 64000, 128000):
        t1 = random_tree(m)
        t2 = random_tree(n)
        h1 = t1.ipl()/m
        h2 = t2.ipl()/n
        t3=better_merge(t1.to_list(),t2.to_list())
        h3 = t3.ipl()/(n+m)
        t4 = random_tree(n+m)
        h4 = t4.ipl()/(n+m)
        print(f'{n:6d} {h1:5.1f}, {h2:5.1f}, {h3:5.1f}, {h4:5.1f}')


if __name__ == '__main__':
    main()



# Så det andra alternativet  kostar med rad 1-3 n*n för om iter går igenom ittererar den
#Över samtliga n. Förta delan kosta n för den minns varje gång den kör

#Att den växer så pass mycket är självklart. Det beror på att när vi mergar dem så lägger
#Vi till i slutet av trädet och den fortsätter byggas på det viset, dvs att det finns
#Många noder som hade varit mer optimala högre upp men som in kan läggas där på grund
#Av att platserna är upptagna, bättre sätt hade varit att byta ner alla noder
#Och därmed bygga upp den vägen. Det kan komma och ta längre tid