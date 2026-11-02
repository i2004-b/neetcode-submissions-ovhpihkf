class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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