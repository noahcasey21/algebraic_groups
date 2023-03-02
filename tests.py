import unittest
from cayley import Cayley

class TestPerms(unittest.TestCase):

    t_cayley = Cayley(4)

    def test_composition(self):
        ans = [4,1,3,2]
        sol = self.t_cayley.compose([2,3,4,1],[3,4,2,1])

        self.assertListEqual(ans, sol)

        

if __name__ == '__main__':
    unittest.main()