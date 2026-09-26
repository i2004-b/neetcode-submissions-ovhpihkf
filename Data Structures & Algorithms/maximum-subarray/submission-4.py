class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Declare a cache to hold visited values
        cache = {}

        # Recursive function
        def dfs(i, flag):
            # Base case: check if measurement already in cache
            if (i, flag) in cache:
                return cache[(i, flag)]

            # Base case: last index
            if i == len(nums) - 1:
                if flag:
                    cache[(i, flag)] = max(0, nums[i])
                else:
                    cache[(i, flag)] = nums[i]

                return cache[(i, flag)]

            # If flag is true
            if flag:
                cache[(i, flag)] = max(0, nums[i] + dfs(i + 1, flag))
            else:
                cache[(i, flag)] = max(dfs(i + 1, flag), nums[i] + dfs(i + 1, not flag))

            return cache[(i, flag)]

        return dfs(0, False)
            
            