"""
Binary Representation Problem

This program converts a decimal integer N to its binary representation
and outputs it as a 10-digit string with leading zeros if necessary.
"""


def binary_representation_original(num: int) -> str:
    """
    Convert a decimal number to binary representation using the original approach.
    
    This is the original implementation which:
    1. Repeatedly divides the number by 2 and collects remainders
    2. Builds the binary representation from right to left
    3. Pads with leading zeros to ensure 10 digits
    
    Args:
        num: A decimal integer (1 ≤ num ≤ 1000)
        
    Returns:
        A 10-digit binary representation as a string
    """
    arr = []
    while num > 0:
        remainder = num % 2
        arr.append(remainder)
        num //= 2

    while len(arr) < 10:
        arr.append(0)

    arr.reverse()

    arr_ = [str(x) for x in arr]
    return "".join(arr_)


def binary_representation(num: int) -> str:
    """
    Convert a decimal number to binary representation using bit shifts.
    
    This implementation follows the C++ solution approach:
    1. Processes each bit position from most significant to least significant (left to right)
    2. Uses bit operations to determine if a bit is set
    3. Outputs exactly 10 digits with leading zeros
    
    Args:
        num: A decimal integer (1 ≤ num ≤ 1000)
        
    Returns:
        A 10-digit binary representation as a string
    """
    # Validate input
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    if not (1 <= num <= 1000):
        raise ValueError("Input must be between 1 and 1000 inclusive")
    
    result = ""
    # Process each bit position from most significant (9) to least significant (0)
    for x in range(9, -1, -1):
        # Calculate 2^x
        power = 1 << x
        # Check if the bit at position x is set
        bit = (num // power) % 2
        result += str(bit)
    
    return result


def binary_representation_builtin(num: int) -> str:
    """
    Convert a decimal number to binary representation using Python's built-in bin() function.
    
    Args:
        num: A decimal integer (1 ≤ num ≤ 1000)
        
    Returns:
        A 10-digit binary representation as a string
    """
    # Validate input
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    if not (1 <= num <= 1000):
        raise ValueError("Input must be between 1 and 1000 inclusive")
    
    # Convert to binary and remove '0b' prefix
    binary = bin(num)[2:]
    
    # Pad to 10 digits
    return binary.zfill(10)


def main():
    """Main function to handle input and output."""
    try:
        # Get input from user
        n = int(input().strip())
        
        # Validate input range
        if not (1 <= n <= 1000):
            raise ValueError("Input must be between 1 and 1000 inclusive")

        # Calculate binary representation
        # Uncomment the implementation you want to use:
        binary = binary_representation(n)
        # binary = binary_representation_original(n)
        # binary = binary_representation_builtin(n)

        # Output the result
        print(binary)

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
