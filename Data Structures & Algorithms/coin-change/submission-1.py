class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a dp array with max value set to infinity
        # Have the length be amount + 1 so that the indices are depicted
        dp = [float("inf")] * (amount + 1)

        # Set location 0 to 0 as there you need 0 coins to make 0 cents
        dp[0] = 0

        # Iterate through the cents to make
        for i in range(1, amount + 1):
            # Iterate over the coin options that are available
            for c in coins:
                # Check if the cents - coin is greater than or equal to 0
                if i - c >= 0:
                    # Update the value
                    dp[i] = min(dp[i], 1 + dp[i - c]) # The 1 comes from the current coin

        return dp[-1] if dp[-1] < float("inf") else -1