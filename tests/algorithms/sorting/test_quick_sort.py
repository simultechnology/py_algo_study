"""
Tests for the Quick Sort algorithm
"""
import pytest

from py_algo_study.algorithms.sorting.quick_sort import quick_sort


def test_quick_sort_with_integers():
    """Test sorting an array of integers"""
    # Arrange
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected


def test_quick_sort_with_strings():
    """Test sorting an array of strings"""
    # Arrange
    unsorted = ["banana", "apple", "cherry", "date"]
    expected = ["apple", "banana", "cherry", "date"]
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected


def test_quick_sort_with_empty_array():
    """Test sorting an empty array"""
    # Arrange
    unsorted = []
    expected = []
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected


def test_quick_sort_with_single_element():
    """Test sorting an array with a single element"""
    # Arrange
    unsorted = [42]
    expected = [42]
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected


def test_quick_sort_with_duplicate_elements():
    """Test sorting an array with duplicate elements"""
    # Arrange
    unsorted = [3, 3, 3, 2, 2, 1, 1]
    expected = [1, 1, 2, 2, 3, 3, 3]
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected


def test_quick_sort_with_negative_numbers():
    """Test sorting an array with negative numbers"""
    # Arrange
    unsorted = [5, -10, 0, 15, -5]
    expected = [-10, -5, 0, 5, 15]
    
    # Act
    result = quick_sort(unsorted)
    
    # Assert
    assert result == expected
