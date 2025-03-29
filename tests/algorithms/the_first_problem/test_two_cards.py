"""
Tests for the Two Cards Problem
"""
import pytest
from unittest.mock import patch
import io
import sys

from py_algo_study.algorithms.the_first_problem.two_cards import is_sum_possible, main


class TestTwoCards:
    """Test cases for the Two Cards problem."""

    def test_is_sum_possible_true(self):
        """Test is_sum_possible when a valid combination exists."""
        # Test a simple case where a sum is possible
        assert is_sum_possible(10, [1, 4], [6, 9]) == True
        
        # Test when only one combination works
        assert is_sum_possible(10, [1, 5, 9], [2, 4, 6]) == True

    def test_is_sum_possible_false(self):
        """Test is_sum_possible when no valid combination exists."""
        # Test the example case from the problem
        assert is_sum_possible(100, [17, 57, 99], [10, 36, 53]) == False
        
        # Test another case
        assert is_sum_possible(20, [1, 5], [2, 4]) == False

    @patch('builtins.input', side_effect=['2 10', '1 5', '5 9'])
    def test_main_possible(self, mock_input):
        """Test main function when a valid combination exists."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "Yes"

    @patch('builtins.input', side_effect=['3 100', '17 57 99', '10 36 53'])
    def test_main_impossible(self, mock_input):
        """Test main function when no valid combination exists."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "No"

    @patch('builtins.input', side_effect=['101 50', '17 57 99', '10 36 53'])
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

    @patch('builtins.input', side_effect=['3 100', '17 57', '10 36 53'])
    def test_main_red_cards_length_mismatch(self, mock_input):
        """Test main function when the red cards array length doesn't match N."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert "Error" in captured_output.getvalue()
        assert "Expected 3 integers for red cards" in captured_output.getvalue()
