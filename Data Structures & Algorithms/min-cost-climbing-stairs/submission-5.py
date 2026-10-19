class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        def dfs(ind):
            # Check if the index is at the end
            if ind == len(cost):
                return 0
            if ind > len(cost):
                return 1e9

            min_cost = 0

            # Run dfs on both routes
            min_cost = cost[ind] + min(dfs(ind + 1), dfs(ind + 2))

            return min_cost

        return min(dfs(0), dfs(1))
        """

        # Add caching
        cache = {}
        self.length = len(cost)
        cache[self.length] = 0

        def dfs(ind):
            if ind in cache:
                return cache[ind]

            cache[ind] = 0

            cache[ind] = cost[ind] + min(dfs(ind + 1), dfs(ind + 2) if ind + 2 < self.length + 1 else 0)

            return cache[ind]

        return min(dfs(0), dfs(1))


            