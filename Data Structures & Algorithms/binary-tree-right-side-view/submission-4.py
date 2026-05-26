# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case: the root does not exist
        if not root:
            return []
        
        # Create array that holds the rightmost values
        right = []

        # Create a stack that initially holds a tuple of the root and its depth (0)
        stack = [(root, 0)]

        # Iterate while the stack is non empty
        while stack:
            # Pop and unpack from the stack
            node, depth = stack.pop()
            # Add value from depth to the array is the length of the array is not greater than the depth
            if depth == len(right):
                right.append(node.val)

            # Add non-NULL values to the stack
            # Add right value second so you can pop it out first
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        # Return the right list
        return right