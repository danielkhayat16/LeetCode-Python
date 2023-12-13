class Solutions:
    # LeetCode .1 Two sum
    # Given an array of integers return the indices of the two numbers that sums up to a given target
    def twoSum(self, arr, target):
        hashMap = {}
        for i, num in enumerate(arr):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i
        return

    #LeetCode .121 - Best Time to buy and sell stock
    def buySellStocks(self, arr):
        buyDay = 0 # At the beggining we must initiate the firsst two day at 0 and 1.
        sellDay = 1
        tmpMax = -1 # Initiate a temporary maximum value to iterate over the array.
        while sellDay < len(arr) :
            if(arr[buyDay] < arr[sellDay]):
                profit = arr[sellDay] - arr[buyDay]
                tmpMax = profit if profit > tmpMax else tmpMax
            else :
                buyDay = sellDay
            sellDay += 1
        return tmpMax           