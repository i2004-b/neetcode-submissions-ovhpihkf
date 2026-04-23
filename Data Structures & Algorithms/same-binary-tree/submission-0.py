# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_tree = []
        q_tree = []

        def inorder(root, array):
            if not root:
                array.append(None)
                return None

            array.append(root.val)
            inorder(root.left, array)
            inorder(root.right, array)

        inorder(p, p_tree)
        inorder(q, q_tree)

        return p_tree == q_tree
