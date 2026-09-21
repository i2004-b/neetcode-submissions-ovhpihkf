class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        # Set first index to 0 as you can make 0 coins with 0 coins
        dp[0] = 0

        # Iterate through indices (which represent different coin amounts)
        for i in range(1, amount + 1):
            # Iterate through coin denominations
            for c in coins:
                # Check that the current amount (index) minus coin is greater than or equal to 0
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return -1 if dp[-1] == float("inf") else dp[-1]