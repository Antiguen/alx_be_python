# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        # This is executed before every single test_ method
        self.calc = SimpleCalculator()

    # --- Test Addition (add) ---
    def test_addition_positive(self):
        """Test addition with two positive numbers."""
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_addition_negative(self):
        """Test addition with positive and negative numbers."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        # Use round() for floating point checks to prevent precision errors
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)

    # --- Test Subtraction (subtract) ---
    def test_subtraction_positive(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_negative(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    # --- Test Multiplication (multiply) ---
    def test_multiplication_positive(self):
        """Test multiplication with two positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiplication_negative(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 5), -25)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    # --- Test Division (divide) ---
    def test_division_normal(self):
        """Test normal division resulting in an integer."""
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_by_zero(self):
        """Test the edge case: division by zero, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        """Test zero divided by any non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0)


# This allows the tests to run when the script is executed directly
if __name__ == '__main__':
    unittest.main()