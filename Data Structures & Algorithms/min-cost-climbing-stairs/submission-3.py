class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append 0 to cost to represent end
        cost.append(0)

        # Iterate backwards starting at 3rd to last location
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])