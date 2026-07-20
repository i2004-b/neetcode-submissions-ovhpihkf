# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 1
        # Initialize with the root and level 1
        stack = [[root, 1]]

        # Iterate while stack exists
        while stack:
            # pop from the stack
            node, height = stack.pop()
            # Update max_len
            max_len = max(max_len, height)
            # Add values
            if node.right:
                stack.append([node.right, height + 1])
            if node.left:
                stack.append([node.left, height + 1])

        return max_len
