"""
Tests for the Binary Representation Problem
"""
import pytest
from unittest.mock import patch
import io
import sys

from py_algo_study.algorithms.the_first_problem.binary_representation import (
    binary_representation,
    binary_representation_original,
    binary_representation_builtin,
    main
)


class TestBinaryRepresentation:
    """Test cases for the Binary Representation problem."""

    def test_binary_representation_examples(self):
        """Test binary_representation with example cases from the problem."""
        # Example 1: 13 -> 0000001101
        assert binary_representation(13) == "0000001101"
        
        # Example 2: 37 -> 0000100101
        assert binary_representation(37) == "0000100101"
        
        # Example 3: 1000 -> 1111101000
        assert binary_representation(1000) == "1111101000"
    
    def test_binary_representation_original_examples(self):
        """Test binary_representation_original with example cases from the problem."""
        # Example 1: 13 -> 0000001101
        assert binary_representation_original(13) == "0000001101"
        
        # Example 2: 37 -> 0000100101
        assert binary_representation_original(37) == "0000100101"
        
        # Example 3: 1000 -> 1111101000
        assert binary_representation_original(1000) == "1111101000"
    
    def test_binary_representation_builtin_examples(self):
        """Test binary_representation_builtin with example cases from the problem."""
        # Example 1: 13 -> 0000001101
        assert binary_representation_builtin(13) == "0000001101"
        
        # Example 2: 37 -> 0000100101
        assert binary_representation_builtin(37) == "0000100101"
        
        # Example 3: 1000 -> 1111101000
        assert binary_representation_builtin(1000) == "1111101000"
    
    def test_binary_representation_edge_cases(self):
        """Test binary_representation with edge cases."""
        # Minimum value: 1 -> 0000000001
        assert binary_representation(1) == "0000000001"
        
        # Maximum value: 1000 -> 1111101000
        assert binary_representation(1000) == "1111101000"
        
        # Power of 2: 512 -> 1000000000
        assert binary_representation(512) == "1000000000"
        
        # Power of 2 minus 1: 511 -> 0111111111
        assert binary_representation(511) == "0111111111"
    
    def test_binary_representation_invalid_inputs(self):
        """Test binary_representation with invalid inputs."""
        # Value too small
        with pytest.raises(ValueError, match="between 1 and 1000"):
            binary_representation(0)
        
        # Value too large
        with pytest.raises(ValueError, match="between 1 and 1000"):
            binary_representation(1001)
        
        # Non-integer
        with pytest.raises(ValueError, match="must be an integer"):
            binary_representation(3.14)
    
    @patch('builtins.input', return_value='13')
    def test_main_example1(self, mock_input):
        """Test main function with example 1."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "0000001101"
    
    @patch('builtins.input', return_value='37')
    def test_main_example2(self, mock_input):
        """Test main function with example 2."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert captured_output.getvalue().strip() == "0000100101"
    
    @patch('builtins.input', return_value='abc')
    def test_main_invalid_input(self, mock_input):
        """Test main function with invalid input."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert "Error" in captured_output.getvalue()
    
    @patch('builtins.input', return_value='1001')
    def test_main_out_of_range(self, mock_input):
        """Test main function with out-of-range input."""
        # Redirect stdout to capture output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Call the main function
        main()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check the output
        assert "Error" in captured_output.getvalue()
        assert "between 1 and 1000" in captured_output.getvalue()
