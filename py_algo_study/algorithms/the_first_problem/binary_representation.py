
def main():
    """Main function to handle input and output."""
    try:
        # Get input from user
        n = int(input().strip())

        # Calculate binary
        binary = binary_representation(n)

        # Output the result
        print(binary)

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")


def binary_representation(num):
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

if __name__ == "__main__":
    main()
