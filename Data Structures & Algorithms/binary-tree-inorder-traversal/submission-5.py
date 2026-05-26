# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Base Case: return if there is no root
        if not root:
            return []
        
        # List to store traversal order
        traversal = []
        
        # Declare a stack to track the nodes
        stack = []

        # Curr pointer to point to the root
        curr = root

        # Iterate while the stack is non empty or while curr exists
        while stack or curr:
            # Keep going down curr's left children
            while curr:
                # Append curr to the stack
                stack.append(curr)
                # Set curr to curr.left
                curr = curr.left

            # When curr becomes out of bounds, reset it to the top of the stack
            curr = stack.pop()
            # Add value to the traversal list
            traversal.append(curr.val)
            # Set curr to the right child
            curr = curr.right

        # Return the traversal list
        return traversal