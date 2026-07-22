# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS Recursive Re-attempt
        # Complexity Analysis:
        # Time: O(m * n) (think about it as double for loop in that you check every subtree of the same size as subroot through the root tree)
        # Space: O(m + n)

        # Base Cases
        # If subRoot is empty, it is a subtree of the root regardless of whether or not the root is empty
        if not subRoot:
            return True
        
        # If the root is empty but subRoot is not empty (as proven by previous conditional), then return False
        if not root:
            return False

        # Check if the root is the same as the subroot
        if self.same(root, subRoot):
            return True

        # If not true above check that subRoot is a subtree in either the left or the right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    # Declare helper function to check if the tree is the same
    def same(self, x, y):
        # If both are null return true
        if not x and not y:
            return True

        # Continue checking if the current nodes match up
        if x and y and x.val == y.val:
            return self.same(x.left, y.left) and self.same(x.right, y.right)
        else:
            return False