from solutions import Solutions


def main():
    test = Solutions()
    array1 = [1, 2, 3, 4, 5, 67, 8, 9]
    array2 = [6, 7, 2, 9, 6]
    array3 = [-1, 1, 0, 3, -3]
    print(test.twoSum(array1, 68) == [0, 5])
    print(test.buySellStocks(array2) == 7)
    print(test.containsDuplicate(array2) == True)
    print(test.containsDuplicate(array1) == False)
    print(test.productExceptSelf(array3) == [0, 0, 9, 0, 0])
    print(test.maximumProductSubarray([0, 3, -2, 4]) == 4)
    print(test.missingNumber([0, 1, 2]))
    print(test.reverseBits(43261596))
    print(test.numberOfOneBits(8))
    print(4 & 111)

if __name__ == "__main__":
    main()
