# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Return if the root does not exist
        if not root:
            return
        
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Continuously swap on the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root
        return root