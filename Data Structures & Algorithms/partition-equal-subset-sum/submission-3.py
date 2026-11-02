class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        # Brute Force Solution: T: O(2 ^ N), S: O(N)
        def dfs(target, i):
            if i >= len(nums) or target < 0:
                return False

            if target == 0:
                return True

            return dfs(target - nums[i], i + 1) or dfs(target, i + 1)

        total = sum(nums)

        if total % 2:
            return False
        
        return dfs(total // 2, 0)
        """

        # Add caching: T --> O(N), S --> O(N)
        cache = {}

        def dfs(target, i):
            if (target, i) in cache:
                return cache[(target, i)]

            if i >= len(nums) or target < 0:
                return False

            if target == 0:
                cache[(target, i)] = True
                return cache[(target, i)] 
            

            cache[(target, i)] = dfs(target - nums[i], i + 1) or dfs(target, i + 1)

            return cache[(target, i)]

        total = sum(nums)

        if total % 2:
            return False

        return dfs(total // 2, 0)

            

