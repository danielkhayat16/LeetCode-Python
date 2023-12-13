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
