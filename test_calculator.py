import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_pr(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_add_nr(self):
        self.assertEqual(self.calc.add(-1, -3), -4)

    def test_subtract_pr(self):
        self.assertEqual(self.calc.subtract(-1, -3), 2)

    def test_subtract_nr(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        
    def test_multiply_pr(self):
        self.assertEqual(self.calc.multiply(1, 1), 1)

    def test_multiply_nr(self):
        self.assertEqual(self.calc.multiply(1, -2), -2)
        
    def test_divide_pr(self):
        self.assertEqual(self.calc.divide(-3, -2),1)

    def test_divide_nr(self):
        self.assertEqual(self.calc.divide(-2, 1), -2)
        
    def test_modulo_zr(self):
        self.assertEqual(self.calc.modulo(1, 1), 0)

    def test_modulo_nzr(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)
        
if __name__ == '__main__':
    unittest.main()