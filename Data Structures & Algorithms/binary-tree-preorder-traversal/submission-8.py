# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Create list to hold traversal
        traversal = []

        # Create stack to hold nodes
        stack = []

        # Point to the root using curr
        curr = root

        # Iterate while stack is non-empty or if curr exists
        while stack or curr:
            while curr:
                # Add node to the stack
                stack.append(curr)
                traversal.append(curr.val)
                # Set to curr.left
                curr = curr.left

            # When you encounter NULL, pop from stack
            curr = stack.pop()

            # Set curr to the right child
            curr = curr.right

        # Return the traversal list
        return traversal