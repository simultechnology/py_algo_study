"""
Tests for the Square Area Calculator
"""
import pytest
from unittest.mock import patch
import io
import sys

from py_algo_study.algorithms.the_first_problem.square import calculate_area, main


class TestSquareAreaCalculator:
    """Test cases for the Square Area Calculator."""

    def test_calculate_area_valid(self):
        """Test calculate_area with valid inputs."""
        # Test with minimum valid value
        assert calculate_area(1) == 1
        
        # Test with a typical value
        assert calculate_area(5) == 25
        
        # Test with maximum valid value
        assert calculate_area(100) == 10000

    def test_calculate_area_invalid_type(self):
        """Test calculate_area with invalid input types."""
        # Test with non-integer inputs
        with pytest.raises(ValueError, match="Input must be an integer"):
            calculate_area(2.5)
            
        with pytest.raises(ValueError, match="Input must be an integer"):
            calculate_area("2")

    def test_calculate_area_out_of_range(self):
        """Test calculate_area with out-of-range inputs."""
        # Test with values below minimum
        with pytest.raises(ValueError, match="Input must be between 1 and 100 inclusive"):
            calculate_area(0)
        
        # Test with values above maximum
        with pytest.raises(ValueError, match="Input must be between 1 and 100 inclusive"):
            calculate_area(101)

    @patch('builtins.input', return_value='10')
    def test_main_valid_input(self, mock_input):
        """Test main function with valid input."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "100"

    @patch('builtins.input', return_value='abc')
    def test_main_invalid_input_type(self, mock_input):
        """Test main function with invalid input type."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check that error message is displayed
        assert "Error" in captured_output.getvalue()

    @patch('builtins.input', return_value='101')
    def test_main_out_of_range(self, mock_input):
        """Test main function with out-of-range input."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check that error message is displayed
        assert "Error" in captured_output.getvalue()
        assert "between 1 and 100" in captured_output.getvalue()
