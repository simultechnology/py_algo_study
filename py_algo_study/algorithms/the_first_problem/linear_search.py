from numpy.ma.core import true_divide


def main():
    res = linear_search(5, 40, [10, 20, 30, 40, 50])
    print(res)

    res = linear_search(6, 28, [30, 10, 40, 10, 50, 90])
    print(res)

def linear_search(n, x, arr):

    for i in range(n):
        if arr[i] == x:
            return True

    return False

if __name__ == "__main__":
    main()