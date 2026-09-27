class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Set array holding whether or not you can reach the end from there
        dp = [False] * len(nums)
        dp[-1] = True

        # Iterate backwards through the nums array
        for i in range(len(nums) - 2, -1, -1):
            # Iterate through the indices that it can get to
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if dp[j]:
                    dp[i] = True
                    break


        return dp[0]


