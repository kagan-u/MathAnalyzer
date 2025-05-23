# tests/test_basic_math.py
import unittest
from MathAnalyzer import factorial, is_prime, fibonacci 

class TestBasicMath(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
