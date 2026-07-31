# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Better solution --> O(N)

        # Declare member variable
        self.res = float("-inf")

        # Declare the helper dfs function
        def dfs(root):
            # Base case: if the root does not exist, retur 0
            if not root:
                return 0

            # Run dfs on the left and the right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the result as if you are splitting at the node
            self.res = max(self.res, root.val + (left if left > 0 else 0) + (right if right > 0 else 0))

            # Return the max of a direction
            return root.val + max(left, right, 0)

        # Call dfs
        dfs(root)
        return self.res