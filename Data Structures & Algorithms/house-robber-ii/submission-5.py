class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        if len(nums) == 1:
            return nums[0]

        def dfs(ind, end):
            if ind > end:
                return 0

            res = max(dfs(ind + 1, end), nums[ind] + dfs(ind + 2, end))

            return res

        return max(dfs(0, len(nums) - 2), dfs(1, len(nums) - 1))
        """
        if len(nums) == 1:
            return nums[0]
            

        def dfs(ind, end, cache):
            if ind > end:
                return 0
            
            if ind in cache:
                return cache[ind]

            cache[ind] = max(dfs(ind + 1, end, cache), nums[ind] + dfs(ind + 2, end, cache))

            return cache[ind]

        return max(dfs(0, len(nums) - 2, {}), dfs(1, len(nums) - 1, {}))
        
        

        