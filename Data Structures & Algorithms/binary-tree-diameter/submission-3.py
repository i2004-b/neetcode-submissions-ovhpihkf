# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Declare a stack with the root initialized
        stack = [root]

        # Declare a dictionary that will hold heights and diameters
        # The dictionary will be initialized with None mapped to (0, 0) to handle base case
        mp = {None: (0, 0)}

        # Iterate while the stack exists
        while stack:
            # Get the node at the top of the stack but don't pop yet
            node = stack[-1]

            # Check that the node has children and that the children are not in mp yet
            # Check left, right, and then execute calculations (post-order traversal)
            if node.left and node.left not in mp:
                # Add the value to the stack
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                # If the node's left and right children have been mapped, it is not time to calculate the node's height and diameter
                # Pop the node from the stack
                node = stack.pop()

                # Calculate the left height and diameter
                left_h, left_d = mp[node.left]
                # Calculate the right height and diameter
                right_h, right_d = mp[node.right]

                # Add the node to dictionary with heights and diameters
                mp[node] = (1 + max(left_h, right_h), max(left_h + right_h, left_d, right_d))

        return mp[root][1]