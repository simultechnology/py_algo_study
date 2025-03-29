"""
Two Cards Problem

Taro has N red cards with numbers P_1, P_2, ..., P_N written on them, and N blue cards
with numbers Q_1, Q_2, ..., Q_N written on them. He wants to select one red card and 
one blue card so that the sum of the numbers on the selected cards is equal to K.
This program determines whether such a selection is possible.
"""


def is_sum_possible(k: int, red_cards: list[int], blue_cards: list[int]) -> bool:
    """
    Check if it's possible to select one red card and one blue card
    such that their sum equals k.
    
    Args:
        k: The target sum
        red_cards: List of integers on the red cards
        blue_cards: List of integers on the blue cards
        
    Returns:
        True if a combination exists that sums to k, False otherwise
    """
    # Check all possible combinations of one red card and one blue card
    for red_value in red_cards:
        for blue_value in blue_cards:
            if red_value + blue_value == k:
                return True
    
    return False


def main():
    """Main function to handle input and output according to the problem specifications."""
    try:
        # Read first line containing N and K
        n, k = map(int, input().strip().split())
        
        # Validate N and K constraints (1 ≤ N, K ≤ 100)
        if not (1 <= n <= 100) or not (1 <= k <= 100):
            raise ValueError("N and K must be integers between 1 and 100")
        
        # Read second line containing the values on red cards
        red_cards = list(map(int, input().strip().split()))
        
        # Validate red cards array length
        if len(red_cards) != n:
            raise ValueError(f"Expected {n} integers for red cards, but got {len(red_cards)}")
        
        # Validate red cards values
        for value in red_cards:
            if not (1 <= value <= 100):
                raise ValueError("All red card values must be integers between 1 and 100")
        
        # Read third line containing the values on blue cards
        blue_cards = list(map(int, input().strip().split()))
        
        # Validate blue cards array length
        if len(blue_cards) != n:
            raise ValueError(f"Expected {n} integers for blue cards, but got {len(blue_cards)}")
        
        # Validate blue cards values
        for value in blue_cards:
            if not (1 <= value <= 100):
                raise ValueError("All blue card values must be integers between 1 and 100")
        
        # Check if the required sum is possible
        result = is_sum_possible(k, red_cards, blue_cards)
        
        # Output the result in the required format
        print("Yes" if result else "No")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
