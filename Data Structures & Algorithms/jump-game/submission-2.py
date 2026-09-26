class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Recursion with caching

        # Cache will map indices to boolean
        dp = {}

        def dfs(i):
            # Check if already in dp
            if i in dp:
                return dp[i]
            
            # Check if at the end
            if i == len(nums) - 1:
                dp[i] = True
                return dp[i]
            
            # Check if out of bounds
            if i >= len(nums):
                return False

            if nums[i] == 0:
                return False

            # Iterate through the values
            for j in range(1, nums[i] + 1):
                # Set cache to recursive call
                dp[i] = dfs(i + j)

                if dp[i]:
                    return True

            return dp[i]

        return dfs(0)