"""
Square Area Calculator

This program calculates the area of a square given the length of one side.
The input must be an integer N where 1 ≤ N ≤ 100.
"""


def calculate_area(n: int) -> int:
    """
    Calculate the area of a square with side length n.
    
    Args:
        n: The length of one side of the square (1 ≤ n ≤ 100)
        
    Returns:
        The area of the square (n²)
        
    Raises:
        ValueError: If n is not within the valid range [1, 100]
    """
    # Validate input constraints
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 1 or n > 100:
        raise ValueError("Input must be between 1 and 100 inclusive")
        
    # Calculate and return the area
    return n * n


def main():
    """Main function to handle input and output."""
    try:
        # Get input from user
        n = int(input().strip())
        
        # Calculate area
        area = calculate_area(n)
        
        # Output the result
        print(area)
        
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
