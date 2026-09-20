class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Make 2-D array (len(prices) + 2 rows and 2 columns)
        dp = [[0] * 2 for _ in range(len(prices) + 2)]

        # Iterate backwards
        for i in range(len(prices) - 1, - 1, -1):
            # Buying case
            buy = dp[i + 1][0] - prices[i]
            cooldown = dp[i + 1][1]
            dp[i][1] = max(cooldown, buy)

            # Selling case
            sell = dp[i + 2][1] + prices[i]
            cooldown = dp[i + 1][0]
            dp[i][0] = max(cooldown, sell)

        return dp[0][1]