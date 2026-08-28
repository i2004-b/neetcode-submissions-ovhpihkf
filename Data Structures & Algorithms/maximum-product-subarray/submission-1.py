class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Set result to be the maximum of nums
        res = max(nums)

        # Set the maximum and the minimum to be 1 initially
        maxVal, minVal = 1, 1

        # Iterate through every number in nums
        for n in nums:
            # Check if n is 0 and set max and min to 1
            if n == 0:
                minVal, maxVal = 1, 1
                continue

            # Save the current maxVal (used in calculation with minVal)
            tmp = maxVal

            # The maximum is the max of maxVal * the curr value, minVal * curr value, or n itself
            maxVal = max(maxVal * n, minVal * n, n)
            # The minimum is the min of ORIGINAL maxVal * curr val, minval * curr, or n itself
            minVal = min(tmp * n, minVal * n, n)

            # Update result
            res = max(res, maxVal)

        return res
