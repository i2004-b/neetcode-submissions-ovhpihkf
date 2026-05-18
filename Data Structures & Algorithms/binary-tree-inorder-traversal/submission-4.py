# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Declare a stack to hold the nodes that are being visited
        stack = []

        # Make an array to hold the values of the result
        res = []

        # Point to the root and the other nodes
        curr = root

        # Iterate while the curr pointer is non-Null or if the stack is not empty
        while curr or stack:
            # Keep going down the left with the curr pointer
            while curr:
                # Add the curr node to the stack
                stack.append(curr)
                # Update curr to point to curr.left
                curr = curr.left
            
            # Reassign curr, which is currently at NULL, to top element of stack
            curr = stack.pop()
            # Add the value of curr to res
            res.append(curr.val)

            # Reassign curr to check the right
            curr = curr.right

        # Return the res list
        return res