class Group:
    """
    Class for a general group. Will handle basic operations (mult and add)
    determine or take in? identity, inverses
    populate group visualization (everything will begin with terminal before moving to app or site)
    """

    def __init__(self, name, operation):
        self.name = name
        operations = {'add': lambda x, y: x + y, 
                      'mult': lambda x, y: x * y} # needs to be updated to include special group ops
        self.op = operations[operation]
        self.set = [] #need to fix this to be ordered
        self.e = self.get_id() #get identity

    def operate(self, *args):
        #takes in at least one object to perform the operator on (order matters!!)
        #args are ordered objects to be operated on 
        sol = self.e
        for arg in args:
            sol = self.op(sol, arg)
        return sol

    def get_id(self):
        pass

    def get_inv(self, x):
        pass
        #this one is hard, not sure if there is a general form. may have to have limited groups...
        #i.e. matrices and Z (mod n) have different methods to find e


    def show_grp(self):
        pass

    def get_rand_elt(self):
        pass
    

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