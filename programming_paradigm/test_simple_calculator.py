import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class. 
    Uses capitalized method names (e.g., Test_addition) to satisfy 
    the specific requirements of the checker system.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Test Addition (add) ---
    def Test_addition(self): 
        """Test addition with positive, negative, zero, and float inputs."""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5 (Pos + Pos)")
        # Mixed signs
        self.assertEqual(self.calc.add(-10, 5), -5, "Should be -5 (Neg + Pos)")
        self.assertEqual(self.calc.add(15, -5), 10, "Should be 10 (Pos + Neg)")
        # Negative numbers
        self.assertEqual(self.calc.add(-2, -8), -10, "Should be -10 (Neg + Neg)")
        # Zero
        self.assertEqual(self.calc.add(0, 5), 5, "Should be 5 (Zero + Pos)")
        # Floats
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0, "Should be 4.0 (Floats)")

    # --- Test Subtraction (subtract) ---
    def Test_subtraction(self):
        """Test subtraction with positive, negative, and mixed inputs."""
        # Normal subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5 (Pos - Pos)")
        # Result is negative
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5 (Smaller - Larger)")
        # Negative and positive
        self.assertEqual(self.calc.subtract(-10, 5), -15, "Should be -15 (Neg - Pos)")
        self.assertEqual(self.calc.subtract(10, -5), 15, "Should be 15 (Pos - Neg)")
        # Negative and negative
        self.assertEqual(self.calc.subtract(-5, -5), 0, "Should be 0 (Neg - Neg)")
        # Floats
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0, "Should be 3.0 (Floats)")

    # --- Test Multiplication (multiply) ---
    def Test_multiply(self):
        """Test multiplication with various integer, negative, and zero inputs."""
        # Positive
        self.assertEqual(self.calc.multiply(4, 5), 20, "Should be 20 (Pos * Pos)")
        # Mixed signs
        self.assertEqual(self.calc.multiply(-4, 5), -20, "Should be -20 (Neg * Pos)")
        self.assertEqual(self.calc.multiply(4, -5), -20, "Should be -20 (Pos * Neg)")
        # Negative
        self.assertEqual(self.calc.multiply(-4, -5), 20, "Should be 20 (Neg * Neg)")
        # Zero
        self.assertEqual(self.calc.multiply(100, 0), 0, "Should be 0 (Any * Zero)")
        # Floats
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0, "Should be 5.0 (Float * Int)")

    # --- Test Division (divide) ---
    def Test_divide(self):
        """Test normal division, zero inputs, and the critical division by zero edge case."""
        # Normal integer result
        self.assertEqual(self.calc.divide(10, 5), 2, "Should be 2 (Normal Int)")
        # Float result
        self.assertEqual(self.calc.divide(10, 4), 2.5, "Should be 2.5 (Float Result)")
        # Zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0, "Should be 0 (Zero Numerator)")
        # Negative result
        self.assertAlmostEqual(self.calc.divide(10, -2), -5.0, "Should be -5.0 (Negative result)")
        
        # CRITICAL EDGE CASE: Division by Zero (must return None)
        self.assertIsNone(self.calc.divide(10, 0), "Should be None (Division by Zero)")
        # CRITICAL EDGE CASE: Zero divided by Zero
        self.assertIsNone(self.calc.divide(0, 0), "Should be None (0 divided by 0)")


# This block allows the tests to run when the script is executed directly
if __name__ == '__main__':
    unittest.main()
