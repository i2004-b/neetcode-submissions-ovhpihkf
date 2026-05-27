# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Declare a stack to hold nodes
        stack = []
        # Declare traversal array to hold the traversal
        traversal = []
        # Point to the root using curr
        curr = root

        # Iterate while curr or stack exists
        while curr or stack:
            # What to do if curr exists
            if curr:
                # Add the value to the traversal list
                traversal.append(curr.val)
                # Add the node to the stack
                stack.append(curr)
                # Move curr to the right subtree
                curr = curr.right
            # What to do if curr does not exist
            else:
                # Pop from the stack
                curr = stack.pop()
                # Set curr to the left child
                curr = curr.left

        # Reverse the list to get it in proper postorder
        traversal.reverse()
        # Return the list
        return traversal