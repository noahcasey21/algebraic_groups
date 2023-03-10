from itertools import permutations
from group import Group

class Permutation(Group):
    """
    object that creates correspondence with a group, therefore allowing easy manipulation of
    finite groups
    """

    def __init__(self, size):
        #super().__init__(name)
        self.size = size
        self.perms = list(self.gen_perms())
        self.e = self.get_id()
        
    def gen_perms(self):
        #this can blow up easily, might need to find better way to store or 
        #generate on demand
        e = [i for i in range(1, self.size + 1)]

        return permutations(e)

    def get_id(self):
        return self.perms[0]
    
    def get_inv(self, s):
        # for some permutation s
        s = list(s)
        if (all(x == y for x, y in zip(self.e, s))):
            #its own inverse
            return s

        inv = list(self.e)
        for i in range(self.size):
            inv[s[i] - 1] = i + 1
        
        return inv
        
    def operate(self, *argv):
        #order matters, right to left
        #arguments should be entered in order
        argv = list(argv)
        sol = argv.pop(len(argv) - 1) #pop out the rightmost entry

        for i in range(len(argv), 0, -1): #permutations
            tmp = []
            for j in range(self.size): #entries
                tmp.append(argv[i - 1][sol[j] - 1])
            del argv[i - 1]
            sol = tmp

        return sol

    """
    How to create the correspondence?
    """