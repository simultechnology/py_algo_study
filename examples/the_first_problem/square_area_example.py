"""
Example usage of the Square Area Calculator

This script demonstrates how to use the square area calculator
with various inputs and handles errors appropriately.
"""
from py_algo_study.algorithms.the_first_problem.main import calculate_area


def run_examples():
    """Run several examples of the square area calculator."""
    examples = [1, 2, 10, 50, 100]
    
    print("Square Area Calculator Examples")
    print("==============================")
    
    for n in examples:
        try:
            area = calculate_area(n)
            print(f"Area of a square with side length {n}: {area}")
        except ValueError as e:
            print(f"Error with input {n}: {e}")
            
    print("\nTesting invalid inputs:")
    invalid_examples = [0, 101, 2.5, "not_a_number"]
    
    for invalid in invalid_examples:
        try:
            area = calculate_area(invalid)
            print(f"Area of a square with side length {invalid}: {area}")
        except ValueError as e:
            print(f"Error with input {invalid}: {e}")
            
    print("\nInteractive mode:")
    try:
        user_input = input("Enter a side length (1-100): ")
        n = int(user_input)
        area = calculate_area(n)
        print(f"Area of a square with side length {n}: {area}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_examples()
