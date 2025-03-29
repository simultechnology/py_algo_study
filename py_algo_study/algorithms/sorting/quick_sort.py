"""
Implementation of the Quick Sort algorithm
"""
from typing import List, TypeVar

T = TypeVar('T', int, float, str)


def quick_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using the Quick Sort algorithm.
    
    Args:
        arr: The array to sort
        
    Returns:
        A sorted array
    
    Time Complexity:
        Average: O(n log n)
        Worst: O(n²)
    Space Complexity:
        O(log n)
    """
    # Return empty or single-element arrays as is
    if len(arr) <= 1:
        return arr
    
    # Select a pivot (first element in this implementation)
    pivot = arr[0]
    
    # Divide elements into those less than, equal to, or greater than the pivot
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(less) + equal + quick_sort(greater)


if __name__ == "__main__":
    # Usage example
    test_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(test_array)
    print(f"Original array: {test_array}")
    print(f"Sorted array: {sorted_array}")
    
    # Works with string arrays too
    str_array = ["banana", "apple", "cherry", "date"]
    sorted_str_array = quick_sort(str_array)
    print(f"Original string array: {str_array}")
    print(f"Sorted string array: {sorted_str_array}")
