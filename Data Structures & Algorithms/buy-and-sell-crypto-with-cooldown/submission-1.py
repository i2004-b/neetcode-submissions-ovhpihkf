class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare hashmap that will cache the solutions that have already been seen
        dp = {}

        # Create dfs function to recurse through the prices and find the max_profit
        def dfs(index, buying):
            # Base case #1: index is out of bounds --> return 0
            if index >= len(prices):
                return 0
            
            # Base case #2: index at this state has already been seen in dp
            if (index, buying) in dp:
                return dp[(index, buying)]

            # Check whether you can buy or if you can only sell
            # In both cases, allowed a cooldown
            if buying:
                # Get profit if you buy
                # Keep in mind that you have to subtract current price from the profit as you spent that money
                # Negate the buying boolean
                buy = dfs(index + 1, not buying) - prices[index] # Not including prices[index] in profit, so subtract int
                cooldown = dfs(index + 1, buying)
                max_profit = max(buy, cooldown)
            else:
                # Get profit it you sell
                # If you sell, you cannot buy during the next index so update index by 2; also, add the current price that you got from selling
                sell = dfs(index + 2, not buying) + prices[index]
                cooldown = dfs(index + 1, buying)
                max_profit = max(sell, cooldown)

            # Update the cache
            dp[(index, buying)] = max_profit
            # Return the value
            return dp[(index, buying)]

        # Call dfs
        return dfs(0, True)