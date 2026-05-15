# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # More optimized result retry
        # Declare a helper function to help track if each stage is balanced and its height
        # From the bottom up
        def dfs(root):
            # If there NULL, return True and height of 0
            if not root:
                return [True, 0]

            # Call the function recrusively on the left and the right
            left, right = dfs(root.left), dfs(root.right)
            # Find whether or not the two branches are balanced
            balanced = abs(left[1] - right[1]) <= 1
            # When returning, need to take into account not only if the current val if balanced but also previous
            # Add 1 to the height
            return [balanced and left[0] and right [0], 1 + max(left[1], right[1])]

        # Call dfs on the root and return on the boolean value
        return dfs(root)[0]