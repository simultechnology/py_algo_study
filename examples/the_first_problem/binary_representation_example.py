"""
Example usage of the Binary Representation solution

This script demonstrates how to use the different binary representation 
implementation methods with examples from the problem statement.
"""
from py_algo_study.algorithms.the_first_problem.binary_representation import (
    binary_representation,
    binary_representation_original,
    binary_representation_builtin
)


def run_examples():
    """Run the example cases from the problem statement and compare implementation methods."""
    print("Binary Representation Examples")
    print("=============================")
    
    # Example cases from the problem
    examples = [13, 37, 1000]
    
    for num in examples:
        print(f"\nDecimal: {num}")
        
        # Using the bit-shift approach (similar to C++ solution)
        bit_shift_result = binary_representation(num)
        print(f"Bit-shift approach:   {bit_shift_result}")
        
        # Using the original approach
        original_result = binary_representation_original(num)
        print(f"Original approach:    {original_result}")
        
        # Using Python's built-in approach
        builtin_result = binary_representation_builtin(num)
        print(f"Built-in approach:    {builtin_result}")
        
        # Verify all methods produce the same result
        assert bit_shift_result == original_result == builtin_result
    
    print("\nAll methods produce correct results!")
    
    # Display binary conversion explanation for the first example
    print("\nDetailed explanation for converting 13 to binary:")
    print("1. Divide 13 by 2: 13 ÷ 2 = 6 remainder 1 → rightmost digit is 1")
    print("2. Divide 6 by 2:   6 ÷ 2 = 3 remainder 0 → next digit is 0")
    print("3. Divide 3 by 2:   3 ÷ 2 = 1 remainder 1 → next digit is 1")
    print("4. Divide 1 by 2:   1 ÷ 2 = 0 remainder 1 → next digit is 1")
    print("5. Reading from left to right: 1101")
    print("6. Pad with leading zeros to get 10 digits: 0000001101")
    
    # Performance comparison (optional)
    print("\nPerformance comparison for larger numbers:")
    large_examples = [123, 456, 789, 999]
    
    for num in large_examples:
        print(f"\nDecimal: {num}")
        result = binary_representation(num)
        print(f"Binary: {result}")


if __name__ == "__main__":
    run_examples()
