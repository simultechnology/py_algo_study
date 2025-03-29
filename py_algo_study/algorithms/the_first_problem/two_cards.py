
def main():
    res = two_cards(3, 100, [17, 57, 99], [10, 36, 53])
    if res:
        print("yes")
    else:
        print("no")

def two_cards(n, total, arr1, arr2):
    for i in arr1:
        for j in arr2:
            if total == i + j:
                return True

    return False





if __name__ == "__main__":
    main()