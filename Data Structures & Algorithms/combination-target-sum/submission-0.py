class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Array to hold the result
        res = []

        # Helper dfs function that will break into decision tree
        # i is a pointer to the index within nums
        # curr is an array holding current combination
        # total is a variable holding the value the current combination adds up to
        def dfs(i, curr, total):
            # Base Case #1: total == target --> append the combination and break out
            if total == target:
                # Append a copy of curr because making changes to it
                res.append(curr.copy())
                return
            # Base Case #2: if the pointer is out of bounds or the total is greater than the target, break out of it
            if i >= len(nums) or total > target:
                return
            
            # Can take 2 decisions: include or don't include the number

            # Decision 1: Include the number
            # Run dfs including the current number
            curr.append(nums[i])
            # Start index at the same number to include it, pass in curr, and add the number to the total
            dfs(i, curr, total + nums[i])

            # Decision 2: Don't include the number
            # Run dfs without including the number so pop it from curr
            curr.pop()
            # Run dfs starting at the next index to not include the current number
            dfs(i + 1, curr, total) # Total was never changed; it was just that the previous one had total + the number passed as a parameter

        # Call dfs
        dfs(0, [], 0)
        return res