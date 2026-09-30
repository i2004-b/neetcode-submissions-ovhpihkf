class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP Solution

        dp = [1e9] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break

                dp[i] = min(dp[i], 1 + dp[i + j])

        return dp[0]