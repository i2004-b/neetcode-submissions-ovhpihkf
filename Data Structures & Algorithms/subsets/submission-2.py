class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Most "efficient" solution is Brute Force: Backtracking.
        T: O(n * 2^n)
        S: O(n) (O(2^n) for the output list)
        """

        # Have a list to hold the results
        res = []

        # Have an array to create each subset
        subset = []

        # Declare dfs function that takes in as input an index
        def dfs(i):
            # Base Case: if i is out of bounds, add copy of subset to result (as subset will be modified)
            if i >= len(nums):
                # Make sure copy of subset is added
                res.append(subset.copy())
                return

            # Decision 1 is to include nums[i]
            # Append the number to the subset
            subset.append(nums[i])
            # Run dfs on the next element
            dfs(i + 1)
            

            # Decision 2 is to not include nums[i]
            # Pop the number from the stack
            subset.pop()
            # Run dfs on the next element
            dfs(i + 1)

        # Call dfs
        dfs(0)

        # Return res
        return res