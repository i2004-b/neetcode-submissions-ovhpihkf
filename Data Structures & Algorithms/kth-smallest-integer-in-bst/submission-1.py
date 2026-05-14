# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Keep track of which element you are on
        n = 0
        # Keep a stack to keep track of nodes
        stack = []
        # Have a pointer to root that you can use to traverse
        curr = root

        # Iterate while curr exists and the stack is non-empty
        while curr or stack:
            # Go as far left as you can
            while curr:
                stack.append(curr)
                curr = curr.left

            # When you reach null, reassign curr to what is popped from the stack
            curr = stack.pop()
            # Because you are visiting/processing a node, add 1 to n
            n += 1
            # If n == k, return the value of curr
            if n == k:
                return curr.val

            # Assign curr to the right to visit right nodes
            curr = curr.right