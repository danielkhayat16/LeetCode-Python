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

    # LeetCode .121 - Best Time to buy and sell stock
    def buySellStocks(self, arr):
        buyDay = 0  # At the beggining we must initiate the firsst two day at 0 and 1.
        sellDay = 1
        tmpMax = -1  # Initiate a temporary maximum value to iterate over the array.
        while sellDay < len(arr):
            if arr[buyDay] < arr[sellDay]:
                profit = arr[sellDay] - arr[buyDay]
                tmpMax = profit if profit > tmpMax else tmpMax
            else:
                buyDay = sellDay
            sellDay += 1
        return tmpMax

    # LeetCode .217 - Contains Duplicate
    # Given an array of integers, return true if any velue appears at leat twice
    def containsDuplicate(self, arr):
        hashSet = set()
        for num in arr:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

    # LeetCode .238 - Product of array except Self

    def productExceptSelf(self, arr):
        prefix = 1
        postfix = 1
        returnArr = []
        i = 0
        while i + 1 <= len(arr):
            returnArr.append(prefix)
            prefix *= arr[i]
            i += 1
        i = len(arr) - 1
        while i >= 0:
            returnArr[i] *= postfix
            postfix *= arr[i]
            i -= 1
        return returnArr

    # LeetCode .53 Maximum Subarray

    def maximumSubArray(self, nums):
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(currSum, maxSum)
        return maxSum

    # LeetCode .152 Maximum Product Subarray
    # Given an intger array nums, find the contiguous subarray
    # within an array which has the largest product

    def maximumProductSubarray(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min (n * curMin, tmp, n)
            res = max(res, curMax)
        return res