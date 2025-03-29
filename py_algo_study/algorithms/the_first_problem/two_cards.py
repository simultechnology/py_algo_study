def main():
    """Main function to handle input and output according to the problem specifications."""
    try:
        # Read first line containing N and X
        n, k = map(int, input().strip().split())

        # Validate N and X constraints (1 ≤ N, X ≤ 100)
        if not (1 <= n <= 100) or not (1 <= k <= 100):
            raise ValueError("N and X must be integers between 1 and 100")

        # Read second line containing the array of integers
        arr1 = list(map(int, input().strip().split()))
        # Validate array length
        if len(arr1) != n:
            raise ValueError(f"Expected {n} integers, but got {len(arr1)}")
        # Validate array elements
        for a in arr1:
            if not (1 <= a <= 100):
                raise ValueError("All array elements must be integers between 1 and 100")

        # Read second line containing the array of integers
        arr2 = list(map(int, input().strip().split()))
        # Validate array length
        if len(arr2) != n:
            raise ValueError(f"Expected {n} integers, but got {len(arr2)}")
        # Validate array elements
        for a in arr2:
            if not (1 <= a <= 100):
                raise ValueError("All array elements must be integers between 1 and 100")

        # Perform the search
        result = two_cards(n, k, arr1, arr2)

        # Output the result in the required format
        print("Yes" if result else "No")

    except ValueError as e:
        print(f"Error: {e}")

def two_cards(n, total, arr1, arr2):
    for i in arr1:
        for j in arr2:
            if total == i + j:
                return True

    return False





if __name__ == "__main__":
    main()