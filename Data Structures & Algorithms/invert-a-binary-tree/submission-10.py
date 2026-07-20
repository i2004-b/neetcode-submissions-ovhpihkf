# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Declare stack
        stack = []
        # Add the root to the stack
        stack.append(root)

        # Iterate while stack
        while stack:
            # Pop from stack
            node = stack.pop()
            # Swap the children
            node.left, node.right = node.right, node.left

            # Insert children
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root