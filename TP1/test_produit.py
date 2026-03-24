import unittest
from produit_tableau import produit_des_autres

class TestProduit(unittest.TestCase):

    def test1(self):
        self.assertEqual(produit_des_autres([1,2,3,4,5]), [120,60,40,30,24])

    def test2(self):
        self.assertEqual(produit_des_autres([3,2,1]), [2,3,6])

if __name__ == "__main__":
    unittest.main()
