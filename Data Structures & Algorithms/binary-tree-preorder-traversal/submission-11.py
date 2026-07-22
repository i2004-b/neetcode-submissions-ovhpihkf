# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Declare the stack
        stack = []
        # Declare array to hold values
        arr = []
        # Point to the current node with pointer
        curr = root

        while curr or stack:
            # Iterate going down the left with curr
            while curr:
                # Add the value
                arr.append(curr.val)
                # Add the right child to the stack if non-Null
                stack.append(curr.right)
                # Move the curr pointer to the left
                curr = curr.left
            
            # When null, reassign curr to what is popped from the stack
            curr = stack.pop()

        return arr