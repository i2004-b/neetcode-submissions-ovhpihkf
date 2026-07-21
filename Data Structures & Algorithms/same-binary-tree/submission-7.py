# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_array = []
        q_array = []

        def preorder(root, arr):
            if not root:
                arr.append("None")
                return 

            arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)

        preorder(p, p_array)
        preorder(q, q_array)
        return p_array == q_array
