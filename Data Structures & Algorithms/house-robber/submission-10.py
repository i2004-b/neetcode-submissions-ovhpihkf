class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(ind):
            if ind in cache:
                return cache[ind]

            if ind >= len(nums):
                return 0
            

            cache[ind] = max(dfs(ind + 1), nums[ind] + dfs(ind + 2))

            return cache[ind]

        return dfs(0)