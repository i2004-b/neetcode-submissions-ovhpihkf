class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 2-D array 
        dp = [[0] * len(nums) for _ in range(2)]

        # Initialize curr_sum
        dp[0][0] = nums[0]
        # Initialize max_sum
        dp[1][0] = nums[0]

        # Iterate through the array
        for i in range(1, len(nums)):
            dp[0][i] = dp[0][i - 1] + nums[i] if dp[0][i - 1] >= 0 else nums[i]
            dp[1][i] = max(dp[1][i - 1], dp[0][i])

        return dp[1][len(nums) - 1]
