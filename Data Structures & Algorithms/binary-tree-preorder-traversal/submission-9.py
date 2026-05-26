# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Second version of the iterative solution requires no extra loop within, but simplifies it using a conditional
        # Declare an array to hold the traversal elements
        traversal = []

        # Declare a stack to hold the nodes
        stack = []

        # Set a pointer to root
        curr = root

        # Iterate while the stack or curr exists
        while stack or curr:
            # If curr
            if curr:
                # Add the node to the stack
                stack.append(curr)
                # Add the value to the traversal list
                traversal.append(curr.val)
                # Set curr to the left child
                curr = curr.left
            # What to do if curr is NULL
            else:
                # Pop from the stack
                curr = stack.pop()
                # Assign curr to the right child
                curr = curr.right

        # Return the traversal array
        return traversal