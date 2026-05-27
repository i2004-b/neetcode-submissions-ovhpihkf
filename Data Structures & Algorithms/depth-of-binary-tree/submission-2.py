# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check base case: if the root does not exist
        if not root:
            return 0
        
        # Set the max_depth to 0
        max_depth = 0

        # Declare a stack with the root initialized at depth 1
        stack = [(root, 1)]

        # Iterate while the stack is non-empty
        while stack:
            # Pop from the stack and unpack the values
            curr, depth = stack.pop()

            # Update the max_depth
            max_depth = max(max_depth, depth)

            # Add children to the stack if non-Null, with their depths
            if curr.right:
                stack.append((curr.right, depth + 1))
            if curr.left:
                stack.append((curr.left, depth + 1))

        # Return the max_depth
        return max_depth