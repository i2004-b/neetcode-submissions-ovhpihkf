class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        def dfs(ind):
            if ind == len(nums) - 1:
                return 0

            step = float("inf")

            for i in range(1, nums[ind] + 1):
                if ind + i == len(nums):
                    break

                step = min(dfs(ind + i) + 1, step)

            return step

        return dfs(0)
        """
        cache = {}
        cache[len(nums) - 1] = 0

        def dfs(ind):
            if ind in cache:
                return cache[ind]

            cache[ind] = float("inf")

            for i in range(1, nums[ind] + 1):
                if ind + i == len(nums):
                    break

                cache[ind] = min(dfs(ind + i) + 1, cache[ind])

            return cache[ind]

        return dfs(0)