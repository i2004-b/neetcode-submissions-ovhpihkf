class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        # Brute Force: T: O(n^2), S: O(1)
        # Double for loop iterating through every possible subarray

        res = max(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                prod *= nums[j]
                res = max(res, prod)

        return res
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

