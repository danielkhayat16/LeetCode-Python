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
            curMin = min(n * curMin, tmp, n)
            res = max(res, curMax)
        return res

    # LeetCode .154 Finding the min value in a sorted array that have been pivoted once

    def findMin(self, nums):
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

    def search(self, nums, target) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
    # LeetCode 11 Container with most Water
    # You are given an integer array height of length n. Find two lines that together with the x-axis form a container, such that the container contains the most water.
    # Return the maximum amount of water a container can store.
    def containerWithMostWater(self, nums):
        l, r = 0, len(nums)
        res = 0
        while(l < r):
            curr = (r -l) * min (nums[r], nums[r])
            res = max(res, curr)
            if(nums[l] > nums[r]):
                r  -= 1
            else:
                l += 1
        return res
    
    #LeetCode 191 Number of 1 Bits
    def numberOfOneBits(self, num):
        res = 0
        # First solution using modula
        # while num: 
        #     if( num % 2 == 1):
        #         res += 1
        #     num = num >> 1
        while num:
            num &= (num-1)
            res += 1
        return res
    
    #LeetCode 338 CountingBits
    def countingBits(self, n):
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

    # LeetCode 268 MissingNumber
    def missingNumber(self, nums):
        numsSum = 0
        for i in range(len(nums)):
            numsSum += i - nums[i]
        numsSum += len(nums)
        return numsSum
    # LeetCode 190 Reverse Bits - Binary
    def reverseBits(self, num):
        res = 0
        for i in range(32):
            bit = (num >> i) & 1
            res = res | (bit << (31 - i))
        return res

    # Leetcode 70 Climbing stairs
    def climbingStairs(self, n):
        one, two = 1, 1
        res = one
        for i in range(n - 1):
            res = one + two
            two = one
            one = res + one

        return res