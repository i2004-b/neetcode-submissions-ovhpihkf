# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS solution
        # Complexity: T: O(n), S: O(n)

        # Declare stack, initialized with the root
        stack = [root]
        # Declare map that maps each node to the height and diameter)
        # Initialized with None: (0, 0) so that when the node reaches the end, it does not cause an error
        mp = {None: (0, 0)}

        # Iterate while the stack exists
        while stack:
            # The node you want to look at is the last one, but don't pip yet
            node = stack[-1]

            # Organize this way as we are doing a post-order traversal

            # Check that the left node exists and that it is not in mp
            if node.left and node.left not in mp:
                stack.append(node.left)
            # Check that the right node exists and that it is not in mp
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                # Now pop the node from the stack
                node = stack.pop()

                # Get the left measurements
                left_h, left_d = mp[node.left]
                # Get the right measurements
                right_h, right_d = mp[node.right]

                # Put the height and diameter in for the popped node
                # For diameter, you put all diameters in because you want at the end for the max diameter to just be in the spot where root is
                mp[node] = (1 + max(left_h, right_h), max(left_h + right_h, left_d, right_d))


        return mp[root][1]
