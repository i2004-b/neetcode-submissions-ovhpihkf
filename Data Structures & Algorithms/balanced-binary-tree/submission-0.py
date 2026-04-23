# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n)
        # Create an inner function to run DFS
        # The inner function is needed so that we can keep track of the balance as well as the height

        def dfs(root):
            # Base case
            if not root:
                return [True, 0]

            # Set variables (2-element lists eventually)
            # Set them equal to DFS recursion calls
            left, right = dfs(root.left), dfs(root.right)

            # Get the boolean value for Balance
            # It is true if the left and right are both balanced and if the difference in height is <= 1
            balance = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

            # Return the two-element array
            # For height, add 1 to the greatest sub-tree
            return [balance, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]