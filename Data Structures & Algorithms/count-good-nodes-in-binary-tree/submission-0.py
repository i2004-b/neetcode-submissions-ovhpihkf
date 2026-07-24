# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Set count variable outside of helper function
        self.count = 0

        # Declare helper function
        def dfs(node, max_val):
            # Base Case: If the node does not exist, return
            if not node:
                return

            # If the node.val is greater than or equal to max, update count and max
            if node.val >= max_val:
                self.count += 1
                max_val = node.val

            # Run dfs on the left and the right
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        # Run dfs
        dfs(root, root.val)
        # Return count
        return self.count