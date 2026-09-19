class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Make a 2-D array with n + 1 rows and 2 columns: column 1 for sell and column 2 for buy
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        # Iterate backwards through the list of prices
        for i in range(len(prices) - 1, -1, -1):
            # Case when you buy
            buy = dp[i + 1][0] - prices[i]
            cool_buy = dp[i + 1][1]
            dp[i][1] = max(buy, cool_buy)

            # Case when you sell
            sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
            cool_sell = dp[i + 1][0]
            dp[i][0] = max(sell, cool_sell)

        return dp[0][1]