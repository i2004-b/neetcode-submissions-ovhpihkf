class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n) time and space
        # This method uses the dp array to track how much it costs to get to the index

        # Get length of cost array
        n = len(cost)

        # dp array prefilled with 0s with length n + 1
        dp = [0] * (n + 1)

        # Iterate starting at index 2 (3rd spot as it doesn't cost anything to start at either 0 or 1)
        for i in range(2, n + 1):
            # Min of cost from prev or cost from two before
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]