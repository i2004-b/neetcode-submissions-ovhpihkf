class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Can add caching to the recursive to make it better

        # Cache
        cache = {}

        def dfs(i, flag):
            # Check if value in cache
            if (i, flag) in cache:
                return cache[(i, flag)]
                
            # Check if at the end of the List
            if i == len(nums) - 1:
                # Decide what to return depending on flag
                if flag:
                    # Return the max of 0 and the num
                    cache[(i, flag)] = max(0, nums[i])
                else:
                    # Return the final number as a new subarray of its own
                    cache[(i, flag)] = nums[i]

                return cache[(i, flag)]

            # Check if flag is true
            if flag:
                # Return the maximum of either 0 (ending subarray) or including number + doing dfs
                cache[(i, flag)] = max(0, nums[i] + dfs(i + 1, flag))
            else:
                # Return the maximum of whether or not a subarray should be startec
                cache[(i, flag)] = max(nums[i] + dfs(i + 1, not flag), dfs(i + 1, flag))

            return cache[(i, flag)]

        return dfs(0, False)