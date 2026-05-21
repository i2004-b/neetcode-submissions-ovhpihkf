# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative DFS attempt
        # Declare stack to keep track of the right nodes
        stack = []
        # Set curr to point to root
        curr = root

        # Iterate while curr is non-Null or stack is non-empty
        while curr or stack:
            # If curr exists, swap the left and the right
            if curr:
                curr.left, curr.right = curr.right, curr.left
                # Append the right subtree to the stack
                stack.append(curr.right)
                # Reassign curr to curr.left
                curr = curr.left
            # If curr does not exist
            else:
                curr = stack.pop()

        return root