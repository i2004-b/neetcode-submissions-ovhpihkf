# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS Result
        # Declare stack initiated with the root and the depth of 1
        stack = [[root, 1]]
        # Initialize result to 0
        result = 0

        # Iterate while the stack is non-empty
        while stack:
            # Extract the node and the depth
            node, depth = stack.pop()

            # If the node exists, do the following
            if node:
                # Update the result to be the maximum of the result or depth
                result = max(result, depth)
                # Append the children to the stack
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result