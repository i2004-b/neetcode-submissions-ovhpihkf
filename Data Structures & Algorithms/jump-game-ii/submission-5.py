class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        # Initialize the cache with the end
        cache[len(nums) - 1] = 0

        def dfs(index):
            # Check if in cache
            if index in cache:
                return cache[index]
            
            cache[index] = 1e9

            # Iterate through possible values
            for i in range(1, nums[index] + 1):
                # Check that the length will be valid
                if i + index >= len(nums):
                    break

                cache[index] = min(cache[index], 1 + dfs(i + index))

            return cache[index]

        return dfs(0)