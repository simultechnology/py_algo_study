"""
Example usage of the Two Cards problem solution

This script demonstrates how to use the is_sum_possible function
with the example from the problem statement.
"""
from py_algo_study.algorithms.the_first_problem.two_cards import is_sum_possible


def run_examples():
    """Run the example case from the problem statement and additional examples."""
    print("Two Cards Problem Examples")
    print("=========================")
    
    # Example from the problem statement
    print("\nExample 1:")
    print("Input:")
    print("3 100")
    print("17 57 99")
    print("10 36 53")
    
    k = 100
    red_cards = [17, 57, 99]
    blue_cards = [10, 36, 53]
    
    result = is_sum_possible(k, red_cards, blue_cards)
    print("Output:")
    print("Yes" if result else "No")
    print("Explanation: There is no way to select one red card and one blue card to get a sum of 100.")
    
    # Additional example where a solution exists
    print("\nAdditional Example:")
    print("Input:")
    print("3 70")
    print("17 57 99")
    print("10 36 53")
    
    k = 70
    result = is_sum_possible(k, red_cards, blue_cards)
    print("Output:")
    print("Yes" if result else "No")
    print("Explanation: We can select the red card with value 17 and the blue card with value 53 to get a sum of 70.")
    
    # Show all possible combinations for demonstration
    print("\nAll Possible Combinations in the Additional Example:")
    for red in red_cards:
        for blue in blue_cards:
            sum_value = red + blue
            print(f"Red card {red} + Blue card {blue} = {sum_value}")


if __name__ == "__main__":
    run_examples()
