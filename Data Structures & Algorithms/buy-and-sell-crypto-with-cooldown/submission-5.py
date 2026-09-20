class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare cache to hold values
        dp = {}

        def dfs(index, buying):
            # Base Case 1: index is out of bounds
            if index >= len(prices):
                return 0
            
            # Base Case 2: already been accounted for
            if (index, buying) in dp:
                return dp[(index, buying)]

            # Buy Case
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(buy, cooldown)
            else:
                sell = dfs(index + 2, not buying) + prices[index]
                cooldown = dfs(index + 1, buying)
                dp[(index, buying)] = max(sell, cooldown)

            return dp[(index, buying)]

        dfs(0, True)
        return dp[(0, True)]