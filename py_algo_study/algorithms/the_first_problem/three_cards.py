"""
Three Cards Problem

This program calculates the number of ways to write three integers 
(one on each of red, blue, and white cards) that sum up to K.
Each integer must be between 1 and N inclusive.
"""


def count_combinations(n: int, k: int) -> int:
    """
    Count the number of ways to write three integers (1 ≤ integer ≤ N) on three cards
    such that their sum equals K.
    
    This is the brute force approach with O(N²) time complexity.
    
    Args:
        n: Upper limit for integers (1 ≤ n ≤ 3000)
        k: Target sum (3 ≤ k ≤ 9000)
        
    Returns:
        The number of valid combinations
    """
    # Validate input
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("Inputs must be integers")
    
    if not (1 <= n <= 3000):
        raise ValueError("N must be between 1 and 3000 inclusive")
    
    if not (3 <= k <= 9000):
        raise ValueError("K must be between 3 and 9000 inclusive")
    
    # Initialize counter
    count = 0
    
    # Iterate through possible values for first two cards
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # Calculate the value needed on the third card
            c = k - a - b
            
            # Check if c is within the valid range
            if 1 <= c <= n:
                count += 1
    
    return count


def count_combinations_optimized(n: int, k: int) -> int:
    """
    A more optimized version that reduces unnecessary iterations.
    
    This approach has O(N) time complexity.
    
    Args:
        n: Upper limit for integers (1 ≤ n ≤ 3000)
        k: Target sum (3 ≤ k ≤ 9000)
        
    Returns:
        The number of valid combinations
    """
    # Validate input
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("Inputs must be integers")
    
    if not (1 <= n <= 3000):
        raise ValueError("N must be between 1 and 3000 inclusive")
    
    if not (3 <= k <= 9000):
        raise ValueError("K must be between 3 and 9000 inclusive")
    
    # Initialize counter
    count = 0
    
    # Optimize by considering the valid range for the third card
    for a in range(1, n + 1):
        # The second card can only be in a range where the third card is valid
        # For the third card to be valid: 1 <= (k - a - b) <= n
        # Rearranging: k - a - n <= b <= k - a - 1
        min_b = max(1, k - a - n)
        max_b = min(n, k - a - 1)
        
        # Add the number of valid values for b
        if min_b <= max_b:
            count += (max_b - min_b + 1)
    
    return count


def main():
    """Main function to handle input and output according to the problem specifications."""
    try:
        # Read first line containing N and K
        n, k = map(int, input().strip().split())
        
        # Validate input range
        if not (1 <= n <= 3000):
            raise ValueError("N must be between 1 and 3000 inclusive")
        
        if not (3 <= k <= 9000):
            raise ValueError("K must be between 3 and 9000 inclusive")
        
        # Calculate the result using the optimized solution
        # For large inputs like N=3000, the mathematical solution was not giving correct results
        # so we're using the optimized but reliable solution instead
        result = count_combinations_optimized(n, k)
        
        # Output the result
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
