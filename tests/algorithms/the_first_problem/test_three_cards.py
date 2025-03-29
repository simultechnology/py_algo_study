"""
Tests for the Three Cards Problem
"""
import pytest
from unittest.mock import patch
import io
import sys

from py_algo_study.algorithms.the_first_problem.three_cards import (
    count_combinations,
    count_combinations_optimized,
    main
)


class TestThreeCards:
    """Test cases for the Three Cards problem."""

    def test_count_combinations_examples(self):
        """Test count_combinations with example cases from the problem."""
        # Example 1: n=3, k=6, answer=7
        assert count_combinations(3, 6) == 7
        
        # Example 2: n=3000, k=4000, answer=6498498
        # Note: This is a large test and may be slow with the brute force approach
        # assert count_combinations(3000, 4000) == 6498498
    
    def test_count_combinations_optimized_examples(self):
        """Test count_combinations_optimized with example cases from the problem."""
        # Example 1: n=3, k=6, answer=7
        assert count_combinations_optimized(3, 6) == 7
        
        # Example 2: n=3000, k=4000, answer=6498498
        # This should be much faster than the brute force approach
        assert count_combinations_optimized(3000, 4000) == 6498498
    
    def test_count_combinations_edge_cases(self):
        """Test count_combinations with edge cases."""
        # Minimum valid values: n=1, k=3 (only one combination: 1+1+1)
        assert count_combinations(1, 3) == 1
        
        # No possible combinations: n=1, k=4 (can't reach sum of 4 with max value 1)
        assert count_combinations(1, 4) == 0
        
        # Small case for manual verification
        # For n=2, k=4, the combinations are:
        # (1,1,2), (1,2,1), (2,1,1)
        assert count_combinations(2, 4) == 3
    
    def test_count_combinations_optimized_edge_cases(self):
        """Test count_combinations_optimized with edge cases."""
        # Minimum valid values: n=1, k=3 (only one combination: 1+1+1)
        assert count_combinations_optimized(1, 3) == 1
        
        # No possible combinations: n=1, k=4 (can't reach sum of 4 with max value 1)
        assert count_combinations_optimized(1, 4) == 0
        
        # Small case for manual verification
        assert count_combinations_optimized(2, 4) == 3

    def test_count_combinations_invalid_inputs(self):
        """Test count_combinations with invalid inputs."""
        # N too small
        with pytest.raises(ValueError, match="N must be between 1 and 3000"):
            count_combinations(0, 6)
        
        # N too large
        with pytest.raises(ValueError, match="N must be between 1 and 3000"):
            count_combinations(3001, 6)
        
        # K too small
        with pytest.raises(ValueError, match="K must be between 3 and 9000"):
            count_combinations(3, 2)
        
        # K too large
        with pytest.raises(ValueError, match="K must be between 3 and 9000"):
            count_combinations(3, 9001)
    
    @patch('builtins.input', return_value='3 6')
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
        assert captured_output.getvalue().strip() == "7"
    
    @patch('builtins.input', return_value='3000 4000')
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
        assert captured_output.getvalue().strip() == "6498498"
