# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        curr = root

        # Traverse through the tree using the pointer
        while curr:
            # If the value is greater than both values, move curr to the left
            if max(p.val, q.val) < curr.val:
                curr = curr.left
            # If the value is less than both p and q, move curr to the right
            elif min(p.val, q.val) > curr.val:
                curr = curr.right
            # Else, the value is either p or q or p and q split
            else:
                return curr
