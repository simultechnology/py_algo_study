"""
Tests for the Linear Search Algorithm
"""
import pytest
from unittest.mock import patch
import io
import sys

from py_algo_study.algorithms.the_first_problem.linear_search import linear_search, main


class TestLinearSearch:
    """Test cases for the Linear Search algorithm."""

    def test_linear_search_found(self):
        """Test linear_search when the target value is in the array."""
        # Test the example case where the target is found
        assert linear_search(5, 40, [10, 20, 30, 40, 50]) == True
        
        # Test when the target is at the beginning
        assert linear_search(5, 10, [10, 20, 30, 40, 50]) == True
        
        # Test when the target is at the end
        assert linear_search(5, 50, [10, 20, 30, 40, 50]) == True

    def test_linear_search_not_found(self):
        """Test linear_search when the target value is not in the array."""
        # Test the example case where the target is not found
        assert linear_search(6, 28, [30, 10, 40, 10, 50, 90]) == False
        
        # Test with different values
        assert linear_search(3, 25, [10, 20, 30]) == False

    @patch('builtins.input', side_effect=['5 40', '10 20 30 40 50'])
    def test_main_target_found(self, mock_input):
        """Test main function when the target is found in the array."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "Yes"

    @patch('builtins.input', side_effect=['6 28', '30 10 40 10 50 90'])
    def test_main_target_not_found(self, mock_input):
        """Test main function when the target is not found in the array."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "No"

    @patch('builtins.input', side_effect=['101 40', '10 20 30 40 50'])
    def test_main_invalid_n(self, mock_input):
        """Test main function with invalid N value."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert "Error" in captured_output.getvalue()
        assert "between 1 and 100" in captured_output.getvalue()

    @patch('builtins.input', side_effect=['5 40', '10 20 30 40'])
    def test_main_array_length_mismatch(self, mock_input):
        """Test main function when the array length doesn't match N."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert "Error" in captured_output.getvalue()
        assert "Expected 5 integers" in captured_output.getvalue()
