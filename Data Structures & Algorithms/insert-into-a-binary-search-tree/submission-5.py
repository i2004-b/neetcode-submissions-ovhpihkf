# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            # Search the right subtree
            root.right = self.insertIntoBST(root.right, val)
        # Using else becaused the value is guaranteed not be in the tree
        else:
            # Search the left subtree
            root.left = self.insertIntoBST(root.left, val)

        # return the root
        return root