class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Have a result array to store subsets and return at the end
        result = []

        # Have a subset array that is constantly updated and appended to result
        subset = []

        # Have a helper DFS function goin through from the top to bottom
        # Pass in the index of the number you are at on the list
        def dfs(i):
            # Base case: if you reach the length of the list, then append the subset and return
            if i >= len(nums):
                result.append(subset.copy())
                return

            # There are two decisions you can make to make a subset
            # You can include a number or not include it

            # Decision 1: include the number
            subset.append(nums[i])
            # Run dfs on the next item in the list
            dfs(i + 1)

            # Decision 2: don't include the number, so pop it because it is currently in the list
            subset.pop()
            # Run dfs on the next item in the list
            dfs(i + 1)

        # Run dfs on index 0
        dfs(0)
        # Return the result
        return result