# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Follows the pre-order type of method
        # Declare the stack to hold the nodes
        stack = []

        # Set curr to the root
        curr = root
        # Iterate while curr or root exists
        while curr or stack:
            # If curr exists
            if curr:
                # Swap the children
                curr.left, curr.right = curr.right, curr.left
                # Put the node in the stack
                stack.append(curr)
                # Set curr to its left child
                curr = curr.left
            # What to do if NULL
            else:
                # Pop from the stack
                curr = stack.pop()
                # Reassign to the right child
                curr = curr.right

        # Return the root of the tree
        return root