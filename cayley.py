from itertools import permutations

class Cayley:
    """
    object that creates correspondence with a group, therefore allowing easy manipulation of
    finite groups
    """

    def __init__(self, size):
        self.size = size
        self.perms = list(self.gen_perms())
        self.e = self.perms[0]
        
    def gen_perms(self):
        #this can blow up easily, might need to find better way to store or 
        #generate on demand
        e = [i for i in range(1, self.size + 1)]

        return permutations(e)
    
    #can these be one function?
    def get_inv(self, s):
        # for some permutation s
        if (all(x == y for x, y in zip(self.e, s))):
            #its own inverse
            return s
        
        inv = []
        for i in range(self.size):
            inv[i] = s[i]
        
    def compose(self, *argv):
        #order matters, right to left
        #arguments should be entered in order
        print(argv)
        argv = list(argv)
        sol = argv.pop(len(argv) - 1) #pop out the rightmost entry
        print(argv)

        for i in range(len(argv), 0, -1): #permutations
            tmp = []
            print(f'i = {i}')
            for j in range(self.size): #entries
                print(f'j = {j}')
                tmp.append(argv[i - 1][sol[j] - 1])
            del argv[i - 1]
            sol = tmp

        return sol






        


