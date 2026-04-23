# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # Get the height for both subtrees at each node
        left = self.height(root.left)
        right = self.height(root.right)

        # Return False if the height does not adhere to requirements
        if abs(left - right) > 1:
            return False
            
        # Check both sub-trees for balance
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0

        # Add 1 to each level for the height
        return 1 + max(self.height(root.left), self.height(root.right))