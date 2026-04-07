class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxProf = 0

        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxProf = max(maxProf, profit)
            else:
                i = j
        
        return maxProf