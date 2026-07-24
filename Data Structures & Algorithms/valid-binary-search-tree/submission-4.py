# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Declare helper function to run recursive DFS
        # The helper function will take in the root value and the left and right bounds
        def dfs(root, left, right):
            # If the root does not exist return true
            if not root:
                return True

            # If the root value is not within bounds, return False
            if not (left < root.val < right):
                return False

            # Otherwise run recursion and return the anded result
            # When going to the left, right boundary updated to current value
            # When going to the right, left boundry updated to current value
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        # Run the function and return result
        return dfs(root, float("-inf"), float("inf"))