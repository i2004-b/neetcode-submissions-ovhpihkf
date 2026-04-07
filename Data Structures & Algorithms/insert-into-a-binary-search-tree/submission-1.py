# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # My attempt at iterative after hearing explanation

        if not root:
            return TreeNode(val)
        
        # Save top of the BST
        top = root

        while root:
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
            elif val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break

        return top
