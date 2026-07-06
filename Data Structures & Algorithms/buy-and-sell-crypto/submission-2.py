class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Track the total profit
        profit = 0

        # Set the left pointer to 0
        l = 0

        # Iterate through the list but start r 1 over from l
        for r in range(1, len(prices)):
            # If the value at index r is less than or equal to l, move l over
            if prices[r] <= prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])

        return profit