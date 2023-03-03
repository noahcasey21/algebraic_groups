import unittest
from cayley import Permutation
from numbers import Reals

class TestPerms(unittest.TestCase):

    t4_cayley = Permutation(4)
    t5_cayley = Permutation(5)

    def test_composition(self):
        ans = [4,1,3,2]
        sol = self.t4_cayley.operate([2,3,4,1],[3,4,2,1])

        self.assertListEqual(ans, sol)

    def test_inverse(self):
        ans = [4,1,2,3,5]
        sol = self.t5_cayley.get_inv([2,3,4,1,5])

        self.assertListEqual(ans,sol)

class TestReals(unittest.TestCase):

    a_test = Reals('add')
    m_test = Reals('mult')

    def test_ops(self):
        self.assertEqual(5*4*8, self.m_test.operate(5,4,8))
        self.assertEqual(5+4+8, self.a_test.operate(5,4,8))


if __name__ == '__main__':
    unittest.main()