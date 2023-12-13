from solutions import Solutions

def main():
    test = Solutions()
    array1 = [1, 2, 3, 4, 5, 67, 8, 9]
    array2 = [6, 7, 2, 9, 6]
    print(test.twoSum(array1, 68) == [0,5])
    print(test.buySellStocks(array2) == 7)

if __name__ == "__main__":
    main()