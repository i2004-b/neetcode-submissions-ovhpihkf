class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Have a result list to keep track of all subsets
        result = []

        # Allocate array outside of the function to use for subsets
        subset = []

        # Use a dfs helper function
        # Pass in the index into the function
        def dfs(i):
            # Base case: If the length of the list reached, append the subset and return
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Two decisions: either can icnlude the current number or skip over it
            # Decision 1: include the number
            subset.append(nums[i])
            dfs(i + 1)

            # Decision 2: do not include the current number
            subset.pop()
            dfs(i + 1)

        # Run the dfs function starting at index 0
        dfs(0)

        # Return the result array
        return result