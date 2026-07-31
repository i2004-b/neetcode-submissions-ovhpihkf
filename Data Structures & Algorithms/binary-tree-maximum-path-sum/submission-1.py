# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Brute Force --> O(N^2)

        # Keep a member variable that tracks the result
        self.res = -float("inf")

        # Declare dfs function that checks for the maxPathSum for every node, starting at the root
        def dfs(root):
            # Base case: if the root does not exist, just return
            if not root:
                return

            # Get the max values for the left and the right using a helper function
            left = self.get_max(root.left)
            right = self.get_max(root.right)

            # Update the result with the max sum
            self.res = max(self.res, left + right + root.val)
            # Run dfs on the left and the right
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res



    def get_max(self, root):
        # Base case: if not root, return 0
        if not root:
            return 0

        # Get the max on the left
        left_max = self.get_max(root.left)
        right_max = self.get_max(root.right)
        path = root.val + max(left_max, right_max)

        return max(path, 0)