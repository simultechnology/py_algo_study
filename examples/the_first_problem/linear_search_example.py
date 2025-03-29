"""
Example usage of the Linear Search algorithm

This script demonstrates how to use the linear search algorithm
with the examples from the problem statement.
"""
from py_algo_study.algorithms.the_first_problem.linear_search import linear_search


def run_examples():
    """Run the example cases from the problem statement."""
    print("Linear Search Algorithm Examples")
    print("===============================")
    
    # Example 1
    print("\nExample 1:")
    print("Input:")
    print("5 40")
    print("10 20 30 40 50")
    
    result1 = linear_search(5, 40, [10, 20, 30, 40, 50])
    print("Output:")
    print("Yes" if result1 else "No")
    print("Explanation: 40 is found in the array, so the output is 'Yes'.")
    
    # Example 2
    print("\nExample 2:")
    print("Input:")
    print("6 28")
    print("30 10 40 10 50 90")
    
    result2 = linear_search(6, 28, [30, 10, 40, 10, 50, 90])
    print("Output:")
    print("Yes" if result2 else "No")
    print("Explanation: 28 is not found in the array, so the output is 'No'.")
    
    # Additional examples
    print("\nAdditional Example:")
    print("Input:")
    print("4 10")
    print("10 20 30 40")
    
    result3 = linear_search(4, 10, [10, 20, 30, 40])
    print("Output:")
    print("Yes" if result3 else "No")
    print("Explanation: 10 is found at the beginning of the array, so the output is 'Yes'.")


if __name__ == "__main__":
    run_examples()
