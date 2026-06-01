# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Track the sum with an outside variable
        self.track = 0

        # Declare helper function for backtracking
        def backtrack(root, target):
            # Base case: return False if the node does not exist (but not including leaf nodes)
            if not root:
                return False

            # Add the value to the tracker
            self.track += root.val

            # Check if the value is a leaf node and that the sum equals the target
            if (not root.left and not root.right) and self.track == target:
                return True
            # Check the children
            if backtrack(root.left, target):
                return True
            if backtrack(root.right, target):
                return True

            # Subtract the value if not valid
            self.track -= root.val
            # Return False
            return False

        # Return the result of running the recursive function
        return backtrack(root, targetSum)