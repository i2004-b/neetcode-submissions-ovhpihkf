# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # BRUTE FORCE ATTEMPT --> O(n^2)
        # Base case: return True if there is no root, meaning that it is balanced
        if not root:
            return True

        # Find the heights of the left and the right subtrees
        left, right = self.height(root.left), self.height(root.right)

        # Check if the difference between the heights is good or not
        if abs(left - right) > 1:
            return False

        # Recursive call to check the rest of the nodes
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    # Function for finding the height, which is also a recrusive algo
    def height(self, root):
        # Base case: if there is nothing there, then the height is 0
        if not root:
            return 0

        # Find the height recurively
        left, right = self.height(root.left), self.height(root.right)

        # Return 1 + the max of the subtree heights
        return 1 + max(left, right)


        