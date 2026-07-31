# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Brute Force Solution --> O(N^2)

        # Declare a member variable to hold the final result
        self.res = float("-inf")

        # Declare dfs function
        def dfs(root):
            # Base Case: if the root, does not exist, just return
            if not root:
                return

            # Find the max from the left and the right
            left = self.get_max(root.left)
            right = self.get_max(root.right)

            # Update the result with the sum of the path if greater than result
            self.res = max(self.res, left + root.val + right)

            # Run dfs on the left and the right
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        # Return self.res
        return self.res

    # Declare get_max function to the get the max of a path
    def get_max(self, root):
        # Base case: if the root does not exists, return 0
        if not root:
            return 0

        # Get the sum from the left and right
        left = self.get_max(root.left)
        right = self.get_max(root.right)

        # Find the sum of the path
        path = root.val + max(left, right)
        # Return the path or 0 if the path is negative
        return max(path, 0)
