class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        cache = {}

        def dfs(ind):
            if ind in cache:
                return cache[ind]

            if ind >= len(nums):
                return 0
            

            cache[ind] = max(dfs(ind + 1), nums[ind] + dfs(ind + 2))

            return cache[ind]

        return dfs(0)
        """
        """
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]
        """

        dp0, dp1 = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            dp0, dp1 = max(nums[i] + dp1, dp0), dp0
        
        return dp0