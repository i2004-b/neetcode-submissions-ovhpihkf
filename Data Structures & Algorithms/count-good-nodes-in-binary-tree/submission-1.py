# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Check that the root exists
        if not root:
            return 0

        # Declare count variable
        count = 0

        # Initialize stack with the root and initial max value as a tuple
        stack = [(root, root.val)]

        # Iterate while the stack exists
        while stack:
            # Pop from the stack
            node, max_val = stack.pop()
            # Check that the node is greater than or equal to max_val to check
            if node.val >= max_val:
                # Update count
                count += 1
                # Update max_val
                max_val = node.val
            # Push into stack if the right and left nodes exist
            if node.right:
                stack.append((node.right, max_val))
            if node.left:
                stack.append((node.left, max_val))

        return count
            