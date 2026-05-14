# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function running DFS and keeping track of height
        def dfs(root):
            # Base case: if the root does not exist, return [True, 0]
            if not root:
                return [True, 0]

            # Run DFS on the left and the right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # Check if the value if the height is balanced
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]