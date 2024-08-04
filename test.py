import unittest
from functions import *

class Test_Functions(unittest.TestCase):
    def test_LCM(self):
        self.assertEqual(LCM(36, 48), 144)
        self.assertRaises(ZeroDivisionError, LCM, 0, 0)
        self.assertRaises(ValueError, LCM, "a", 2)
        self.assertRaises(ValueError, LCM, [2], 2)
        self.assertRaises(ValueError, LCM, None, None)

    def test_GCD(self):
        self.assertEqual(GCD(36, 48), 12)
        self.assertRaises(ZeroDivisionError, GCD, 0, 0)
        self.assertRaises(ValueError, GCD, "a", 2)
        self.assertRaises(ValueError, GCD, [2], 2)
        self.assertRaises(ValueError, GCD, None, None)
        


    def test_reducing_a_fraction(self):
        self.assertEqual(reducing_a_fraction_decorator(sum(2, 4, 2, 4), (1, 1)))
    #     self.assertEqual(reducing_a_fraction_decorator(1, 1), (1, 1))
    #     self.assertRaises(ZeroDivisionError, reducing_a_fraction_decorator, 0, 0)
    #     self.assertRaises(ValueError, reducing_a_fraction_decorator, "a", 2)
    #     self.assertRaises(ValueError, reducing_a_fraction_decorator, [2], 2)
    #     self.assertRaises(ValueError, reducing_a_fraction_decorator, None, None)


    def test_sum(self):
        self.assertEqual(sum(4, 10, 3, 10), (7, 10))
        self.assertEqual(sum(5, 2, 4, 10), (29, 10))
        self.assertRaises(ValueError, sum, "a", 2, 2, 2)
        self.assertRaises(ValueError, sum, 2, [2], 2, 2)
        self.assertRaises(ValueError, sum, None, None, None, None)
    
    def test_difference(self):
        self.assertEqual(difference(4, 10, 3, 10), (1, 10))
        self.assertEqual(difference(5, 2, 4, 10), (21, 10))
        self.assertRaises(ValueError, difference, "a", 2, 2, 2)
        self.assertRaises(ValueError, difference, 2, [2], 2, 2)
        self.assertRaises(ValueError, difference, None, None, None, None)

    def test_multiplication(self):
        self.assertEqual(multiplication(1, 5, 1, 2), (1, 10))
        self.assertRaises(ValueError, multiplication, "a", 2, 2, 2)
        self.assertRaises(ValueError, multiplication, 2, [2], 2, 2)
        self.assertRaises(ValueError, multiplication, None, None, None, None)

    def test_dividing(self):
        self.assertEqual(dividing(1, 5, 2, 1), (1, 10))
        self.assertRaises(ValueError, dividing, "a", 2, 2, 2)
        self.assertRaises(ValueError, dividing, 2, [2], 2, 2)
        self.assertRaises(ValueError, dividing, None, None, None, None)
        

if __name__ == "__main__":
  unittest.main()

