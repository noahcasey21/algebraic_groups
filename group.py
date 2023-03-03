from abc import ABC, abstractmethod

class Group(ABC):
    """
    Class for a general group.
    Lists abstract methods plus a couple funtions that don't change between groups
    """

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_inv(self):
        pass

    @abstractmethod
    def operate(self):
        pass

    def cayley_table(self):
        #creates cayley table for groups
        pass
        """should be something like
        for a in elts:
            for b in elts:
                operate (a,b)
                place in table
                operate (b, a)
                place in table"""

    

"""
Types of groups:
----------------
(R*, *)
(R, +)
(C*, *)
Z (mod n)
GLn
SLn
Permutations

----------------
May have to assign isomorphic groups to move around harder ones. i.e. 1-1 correspondence 
between Z (mod n) and perm group may allow us to manipulate perm easier through Z (mod n)
or vice versa: any group can be show to have 1-1 with some perm group. Maybe we could create
some sort of matrix object that allows easy manipulation of objects. Recall this only works for
finite groups

Put on hold until better manipulation technique is determined
"""