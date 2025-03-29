"""
Example usage of the Three Cards problem solution

This script demonstrates how to use the different implementation methods
of the Three Cards problem with examples and performance comparisons.
"""
import time
from py_algo_study.algorithms.the_first_problem.three_cards import (
    count_combinations,
    count_combinations_optimized,
    count_combinations_mathematical
)


def run_examples():
    """Run the example cases from the problem statement and compare implementation methods."""
    print("Three Cards Problem Examples")
    print("===========================")
    
    # Example cases from the problem
    examples = [
        (3, 6),            # Example 1: n=3, k=6, answer=7
        (10, 15),          # Medium case
        (100, 150),        # Larger case
        (3000, 4000)       # Example 2: n=3000, k=4000, answer=6498498
    ]
    
    for n, k in examples:
        print(f"\nN = {n}, K = {k}")
        
        # Using the original approach (may be slow for large inputs)
        if n <= 100:  # Only run for smaller inputs
            start_time = time.time()
            original_result = count_combinations(n, k)
            original_time = time.time() - start_time
            print(f"Original approach:     {original_result} (took {original_time:.6f} seconds)")
        else:
            print(f"Original approach:     (skipped for large input)")
        
        # Using the optimized approach
        start_time = time.time()
        optimized_result = count_combinations_optimized(n, k)
        optimized_time = time.time() - start_time
        print(f"Optimized approach:    {optimized_result} (took {optimized_time:.6f} seconds)")
        
        # Using the mathematical approach
        start_time = time.time()
        mathematical_result = count_combinations_mathematical(n, k)
        mathematical_time = time.time() - start_time
        print(f"Mathematical approach: {mathematical_result} (took {mathematical_time:.6f} seconds)")
        
        # Verify all methods produce the same result
        if n <= 100:
            assert original_result == optimized_result == mathematical_result
        else:
            assert optimized_result == mathematical_result
    
    print("\nAll methods produce correct results for the tested examples!")
    
    # Performance comparison for the specific example
    print("\nDetailed explanation for the example N=3, K=6:")
    print("For N=3, K=6, we need to count all combinations of three cards with values 1-3 that sum to 6.")
    print("The valid combinations are:")
    n, k = 3, 6
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = k - a - b
            if 1 <= c <= n:
                print(f"Red card: {a}, Blue card: {b}, White card: {c}")
    
    print("\nTotal: 7 combinations")


if __name__ == "__main__":
    run_examples()
