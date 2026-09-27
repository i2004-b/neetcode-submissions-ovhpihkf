class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: most optimal
        # Time: O(n); Space: O(1)

        # Set max_count
        max_count = nums[0]
        curr_count = nums[0]

        for i in range(1, len(nums)):
            # Check if current count is less than 0
            if curr_count < 0:
                curr_count = 0

            curr_count += nums[i]
            max_count = max(max_count, curr_count)

        return max_count