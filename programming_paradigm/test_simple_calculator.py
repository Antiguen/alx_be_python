# test_simple_calculator.py (Revised for maximum coverage)

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Test Addition (add) ---
    def test_addition_cases(self):
        """Test addition with positive, negative, and zero inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5 (Pos + Pos)")
        self.assertEqual(self.calc.add(-10, 5), -5, "Should be -5 (Neg + Pos)")
        self.assertEqual(self.calc.add(15, -5), 10, "Should be 10 (Pos + Neg)")
        self.assertEqual(self.calc.add(-2, -8), -10, "Should be -10 (Neg + Neg)")
        self.assertEqual(self.calc.add(0, 5), 5, "Should be 5 (Zero + Pos)")
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0, "Should be 4.0 (Floats)")

    # --- Test Subtraction (subtract) ---
    def test_subtraction_cases(self):
        """Test subtraction with positive, negative, and mixed inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5 (Pos - Pos)")
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5 (Smaller - Larger)")
        self.assertEqual(self.calc.subtract(-10, 5), -15, "Should be -15 (Neg - Pos)")
        self.assertEqual(self.calc.subtract(10, -5), 15, "Should be 15 (Pos - Neg)")
        self.assertEqual(self.calc.subtract(-5, -5), 0, "Should be 0 (Neg - Neg)")
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0, "Should be 3.0 (Floats)")

    # --- Test Multiplication (multiply) ---
    def test_multiplication_cases(self):
        """Test multiplication with various integer and zero inputs."""
        self.assertEqual(self.calc.multiply(4, 5), 20, "Should be 20 (Pos * Pos)")
        self.assertEqual(self.calc.multiply(-4, 5), -20, "Should be -20 (Neg * Pos)")
        self.assertEqual(self.calc.multiply(4, -5), -20, "Should be -20 (Pos * Neg)")
        self.assertEqual(self.calc.multiply(-4, -5), 20, "Should be 20 (Neg * Neg)")
        self.assertEqual(self.calc.multiply(100, 0), 0, "Should be 0 (Any * Zero)")
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0, "Should be 5.0 (Float * Int)")

    # --- Test Division (divide) ---
    def test_division_cases(self):
        """Test normal division, zero inputs, and the division by zero edge case."""
        self.assertEqual(self.calc.divide(10, 5), 2, "Should be 2 (Normal Int)")
        self.assertEqual(self.calc.divide(10, 4), 2.5, "Should be 2.5 (Float Result)")
        self.assertEqual(self.calc.divide(0, 5), 0, "Should be 0 (Zero Numerator)")
        self.assertAlmostEqual(self.calc.divide(10, -2), -5.0, "Should be -5.0 (Negative result)")
        self.assertIsNone(self.calc.divide(10, 0), "Should be None (Division by Zero)")
        self.assertIsNone(self.calc.divide(0, 0), "Should be None (0 divided by 0)")


if __name__ == '__main__':
    unittest.main()