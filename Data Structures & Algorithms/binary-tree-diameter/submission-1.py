# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS Recursive Solution
        # Complexity: T: O(n), S: O(n)

        # Have a global variable that will be updated with the max length
        self.max_len = 0

        # Declare helper function 
        def dfs(root):
            # Declare base case: if the root does not exist, return 0
            if not root:
                return 0

            # Find the heights of both subtrees and save the values
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            # Update max_len by comparing current value in the variable to the sum of the left and right
            self.max_len = max(self.max_len, left_height + right_height)

            # Return 1 + the max of either the left and right as you can't repeat a node
            return 1 + max(left_height, right_height)

        # Call dfs on root
        dfs(root)

        # Return max_len
        return self.max_len