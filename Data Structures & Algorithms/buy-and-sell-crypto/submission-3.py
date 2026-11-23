class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            max_profit = max(max_profit, prices[i] - curr)

        return max_profit