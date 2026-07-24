# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Check that the root exists
        if not root:
            return True

        # Declare a stack that has a tuple with the node and l and right boundaries
        stack = [(root, float("-inf"), float("inf"))]

        # Iterate while stack exists
        while stack:
            # Pop from the stack
            node, left, right = stack.pop()

            # If node value not between boundaries, return false
            if not (left < node.val < right):
                return False

            # Add to the stack with the correct boundaries
            if node.right:
                # The left boundary becomes the current value for the next item
                stack.append((node.right, node.val, right))
            if node.left:
                # The right boundary becomes the current value for the next item
                stack.append((node.left, left, node.val))

        # If it makes it out of the loop, return True
        return True
