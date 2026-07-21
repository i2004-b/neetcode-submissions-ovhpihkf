# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize a stack with p and q in them
        stack = [(p, q)]

        # Iterate while the stack exists
        while stack:
            # Pop the values from the stack
            p_node, q_node = stack.pop()

            # Check the values
            # If both null, continue
            if not p_node and not q_node:
                continue
            # Return false if only one node is NULL or the value is not the same
            elif not p_node or not q_node or p_node.val != q_node.val:
                return False

            # Add the values to the stack, adding the right values first so that you can pop out the left values before
            stack.append((p_node.right, q_node.right))
            stack.append((p_node.left, q_node.left))

        # Return true is successfully iterated through loop
        return True
