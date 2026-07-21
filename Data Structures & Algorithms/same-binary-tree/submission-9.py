# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Better Iterative DFS Solution

        # Check that p and q exist
        if not p and not q:
            return True

        # Stack to hold pairs of nodes
        # Initialize with p and q
        stack = [(p, q)]

        # Iterate while the stack exists
        while stack:
            # Pop the values from the stack
            p_node, q_node = stack.pop()

            if not p_node and not q_node:
                continue
            elif not p_node or not q_node:
                return False
            elif p_node.val != q_node.val:
                return False

            # Append to stack
            # Append the right values first and then the left values
            stack.append((p_node.right, q_node.right))
            stack.append((p_node.left, q_node.left))

        # If you finish the loop successfully, return True
        return True
                
            