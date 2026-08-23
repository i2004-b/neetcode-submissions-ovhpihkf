class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memoization

        dp = [-1] * len(cost)

        def dfs(i):
            # Base Case 1: check if index is out of bounds
            if i >= len(cost):
                return 0

            # If price for index already exists, return it
            if dp[i] > -1:
                return dp[i]

            # Get the cost from here
            price = cost[i] + min(dfs(i + 1), dfs(i + 2))

            # Update array
            dp[i] = price

            return price

        return min(dfs(0), dfs(1))