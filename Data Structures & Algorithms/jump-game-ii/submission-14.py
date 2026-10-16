class Solution:
    def jump(self, nums: List[int]) -> int:
        # Track number of steps needed
        steps = 0

        # Two pointers starting at 0
        l, r = 0, 0

        # Iterate while r is less than the last index
        while r < len(nums) - 1:
            max_ind = -1
            for i in range(l, r + 1):
                max_ind = max(max_ind, i + nums[i])

            l = r + 1
            r = max_ind
            steps += 1

        return steps
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        """