# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Brute Force Solution
        # Complexity: 
        # T: O(n^2) --> checking the height for every single node
        # S: O(n) --> The recursion stack will have every single node in it at max capacity

        # Base case
        if not root:
            return True

        left_h = self.height(root.left)
        right_h = self.height(root.right)

        if abs(left_h - right_h) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)



    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
