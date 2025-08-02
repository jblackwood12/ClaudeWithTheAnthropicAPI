import unittest
from main import calculate_pi

class TestPiCalculation(unittest.TestCase):
    
    def test_pi_calculation(self):
        """Test that the pi calculation is accurate to 5 decimal places."""
        # Known value of pi to 10 decimal places
        actual_pi = 3.1415926536
        
        # Calculate pi to 5 decimal places
        calculated_pi = calculate_pi(5)
        
        # Ensure our calculation is accurate to 5 decimal places
        self.assertEqual(round(actual_pi, 5), calculated_pi)
    
    def test_default_precision(self):
        """Test that the default precision is 5 decimal places."""
        # Calculate pi with default precision
        default_pi = calculate_pi()
        
        # Calculate pi with explicit 5 decimal places
        explicit_pi = calculate_pi(5)
        
        # They should be the same
        self.assertEqual(default_pi, explicit_pi)
    
    def test_pi_value(self):
        """Test that the calculated value is actually close to pi."""
        # The calculated value should be close to 3.14159
        calculated_pi = calculate_pi()
        
        # Test with direct comparison to expected value
        self.assertEqual(calculated_pi, 3.14159)

if __name__ == "__main__":
    unittest.main()