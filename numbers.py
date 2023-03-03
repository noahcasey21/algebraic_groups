from group import Group

class Reals(Group):
    """will handle (R, +), (R*, *), (Q, +), (Q*, *), 
        (Z, +)"""

    def __init__(self, operator):
        operators = {'add': lambda x, y: x + y,
                     'mult': lambda x, y: x * y}
        self.operator = operators[operator]
        self.e = self.get_id()

    def get_id(self):
        if operator is 'add':
            return 0
        else:
            return 1

    def get_inv(self, x):
        if operator is 'add':
            return -x
        else:
            return 1 / x

    def operate(self, *args):
        args = list(args)
        sol = args.pop(len(args) - 1)

        for num in args:
            sol = self.operator(sol, num)

        return sol

