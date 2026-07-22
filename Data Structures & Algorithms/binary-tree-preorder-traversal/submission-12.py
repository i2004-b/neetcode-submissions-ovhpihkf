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
            if curr:
                arr.append(curr.val)
                # Add right to stack
                stack.append(curr.right)
                # Move to the left
                curr = curr.left
            else:
                # Pop from stack to explore new section
                curr = stack.pop()

        return arr