class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Add caching --> more efficient recursion
        # Time: O(n^2); Space: O(n)

        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(nums) - 1:
                cache[i] = True
                return True

            # Loop through the possibilities
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                
                if dfs(i + j):
                    cache[i] = True
                    return True

            cache[i] = False
            return False

        return dfs(0)