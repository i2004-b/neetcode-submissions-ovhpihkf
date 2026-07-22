# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative without extra while loop
        stack = []
        arr = []
        curr = root

        while curr or stack:
            # If curr do the following
            if curr:
                # Add value to the array
                arr.append(curr.val)
                # Add the right child to the stack
                stack.append(curr.right)
                # Move curr to the left
                curr = curr.left
            # If not curr, pop from stack
            else:
                curr = stack.pop()


        return arr