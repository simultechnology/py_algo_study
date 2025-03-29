"""
Linear Search Algorithm

This program determines whether an integer X is included in a list of N integers.
Time limit: 1 second, Difficulty: ★1
"""


def linear_search(n: int, x: int, arr: list[int]) -> bool:
    """
    Search for integer x in an array of integers using linear search.
    
    Args:
        n: Number of elements in the array
        x: The target integer to find
        arr: The array of integers to search in
        
    Returns:
        True if x is found in arr, False otherwise
    """
    for i in range(n):
        if arr[i] == x:
            return True
    return False


def main():
    """Main function to handle input and output according to the problem specifications."""
    try:
        # Read first line containing N and X
        n, x = map(int, input().strip().split())
        
        # Validate N and X constraints (1 ≤ N, X ≤ 100)
        if not (1 <= n <= 100) or not (1 <= x <= 100):
            raise ValueError("N and X must be integers between 1 and 100")
        
        # Read second line containing the array of integers
        arr = list(map(int, input().strip().split()))
        
        # Validate array length
        if len(arr) != n:
            raise ValueError(f"Expected {n} integers, but got {len(arr)}")
        
        # Validate array elements
        for a in arr:
            if not (1 <= a <= 100):
                raise ValueError("All array elements must be integers between 1 and 100")
        
        # Perform the search
        result = linear_search(n, x, arr)
        
        # Output the result in the required format
        print("Yes" if result else "No")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
