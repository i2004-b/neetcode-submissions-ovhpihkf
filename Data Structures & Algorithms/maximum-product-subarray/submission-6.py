class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        # Brute Force: T: O(n^2), S: O(1)
        # Double for loop iterating through every possible subarray

        res = max(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                res = max(res, prod)

        return res
        """

        """
        # Kadane-like algorithm: T: O(n), S: O(1)
        # Use currMax and currMin throughout

        res = max(nums)
        currMin = currMax = 1

        for n in nums:
            # Store the currMax to use in a calculation with currMin
            temp = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * temp, n * currMin, n)
            res = max(res, currMax, currMin)

        return res
        """

        # Prefix and Suffic: T: O(n), S: O(1)
        # Will account for every subarray 
        res = max(nums)
        prefix = suffix = 0
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, prefix, suffix)

        return res


