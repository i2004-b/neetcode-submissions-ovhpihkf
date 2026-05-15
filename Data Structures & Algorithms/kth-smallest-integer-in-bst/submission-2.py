# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Retry of the optimal solution
        # Have a variable to keep track of what node you're at
        n = 0
        # Create stack to hold nodes
        stack = []
        # Point to the root
        curr = root

        # Iterate while the pointer is non-Null or the stack is non-empty
        while curr or stack:
            # Iterate downwards, trying to go as far left as possible
            while curr:
                # Add the node to the stack
                stack.append(curr)
                # Set curr to curr.left
                curr = curr.left

            # Once curr is NULL, assign it to the top value of the stack
            curr = stack.pop()
            # Increment n
            n += 1

            # Check if n is equal to k and return the value if it is
            if n == k:
                return curr.val

            # Check the right side now
            curr = curr.right