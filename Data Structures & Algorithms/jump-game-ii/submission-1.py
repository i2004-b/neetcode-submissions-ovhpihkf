class Solution:
    def jump(self, nums: List[int]) -> int:
        # True caching recursive solution

        cache = {}

        def dfs(i):
            # If at the end, return True
            if i in cache:
                return cache[i]

            if i == len(nums) - 1:
                return 0

            if nums[i] == 0:
                return 1e9
            
            res = 1e9
            
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                res = min(res, 1 + dfs(j))
            
            cache[i] = res
            
            return res

        return dfs(0)