# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative attempt

        # Declare stack to hold the nodes to visit
        stack = []

        # Array to hold values encountered
        arr = []

        # Declare a pointer that will initially point to root
        curr = root

        # Iterate while stack or curr exists
        while stack or curr:
            # Go as far left as possible
            while curr:
                # Add value to stack
                stack.append(curr)
                # Move curr to the left
                curr = curr.left

            # When curr becomes null, pop from stack
            curr = stack.pop()
            # Add value to the arr
            arr.append(curr.val)
            # Set curr to the right
            curr = curr.right

        return arr
