# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = root

        if LCA.val > p.val and LCA.val > q.val:
            return self.lowestCommonAncestor(LCA.left, p, q)
        elif LCA.val < p.val and LCA.val < q.val:
            return self.lowestCommonAncestor(LCA.right, p, q)
        else:
            return LCA