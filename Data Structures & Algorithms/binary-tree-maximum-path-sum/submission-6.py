# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Declare a member variable to hold the result
        # Set the member variable to negative infinity as a tree with all negatives would have a negative number as the minimum, not 0
        self.res = float("-inf")

        # Declare helper dfs function
        def dfs(root):
            # Base Case: if the root does not exist, return 0
            if not root:
                return 0

            # Run dfs on the left and the right
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            # Set the left and the right values to 0 if they are negative
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # Set the result with the split happening at that node
            self.res = max(self.res, root.val + left_max + right_max)

            # Return the greater path without the split
            return root.val + max(left_max, right_max)

        # Call dfs
        dfs(root)
        return self.res