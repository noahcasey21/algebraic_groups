import unittest
from cayley import Cayley

class TestPerms(unittest.TestCase):

    t4_cayley = Cayley(4)
    t5_cayley = Cayley(5)

    def test_composition(self):
        ans = [4,1,3,2]
        sol = self.t4_cayley.compose([2,3,4,1],[3,4,2,1])

        self.assertListEqual(ans, sol)

    def test_inverse(self):
        ans = [4,1,2,3,5]
        sol = self.t5_cayley.get_inv([2,3,4,1,5])

        self.assertListEqual(ans,sol)

if __name__ == '__main__':
    unittest.main()