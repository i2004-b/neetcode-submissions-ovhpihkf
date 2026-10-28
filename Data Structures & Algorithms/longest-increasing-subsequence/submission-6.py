class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            res = max(res, dp[i])

        return res