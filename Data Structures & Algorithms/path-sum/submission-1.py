# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Track the sum
        total = 0

        # Create helper function
        def path_sum(root, total):
            # If the root does not exist return False
            if not root:
                return False
            
            # Add the node value to the total
            total += root.val

            # Check if the node is a leaf node
            if not root.left and not root.right:
                if total == targetSum:
                    return True
                total -= root.val
            
            # Check the left and the right children
            if path_sum(root.left, total):
                return True
            if path_sum(root.right, total):
                return True

            # Return False if nothing is reached
            return False

        return path_sum(root, total)




