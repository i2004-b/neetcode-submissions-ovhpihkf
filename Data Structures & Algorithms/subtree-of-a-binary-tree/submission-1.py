# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS Recursive
        # Complexity:
        # Time (need to check every node for root and subroot): O(m * n)
        # Space (need to check every node for root and subroot): O(m + n)

        # Base case: check if the roots exist
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        # Check the root and the subroot first
        if self.same(root, subRoot):
            return True
        else:
            # Check the two sides
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def same(self, root, subRoot):
        # If both don't exist return true
        if not root and not subRoot:
            return True

        # Continue checking if the nodes exist and the values are the same
        if root and subRoot and root.val == subRoot.val:
            return self.same(root.left, subRoot.left) and self.same(root.right, subRoot.right)
        else:
            return False