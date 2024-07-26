import unittest
import functions

class Test_Functions(unittest.TestCase):
    def test_LCM(self):
        self.assertEqual(functions.LCM(36, 48), 144)
    
    def test_GCD(self):
        self.assertEqual(functions.GCD(36, 48), 12)

    def test_reducing_a_fraction(self):
        self.assertEqual(functions.reducing_a_fraction(36, 48), (3, 4))

    def test_sum(self):
        self.assertEqual(functions.sum(4, 10, 3, 10), (7, 10))
        self.assertEqual(functions.sum(5, 2, 4, 10), (29, 10))
    
    def test_difference(self):
        self.assertEqual(functions.difference(4, 10, 3, 10), (1, 10))
        self.assertEqual(functions.difference(5, 2, 4, 10), (21, 10))

    def test_multiplication(self):
        self.assertEqual(functions.multiplication(2, 5, 5, 2), (10, 10))

    def test_dividing(self):
        self.assertEqual(functions.dividing(2, 5, 2, 5), (10, 10))

if __name__ == "__main__":
  unittest.main()

