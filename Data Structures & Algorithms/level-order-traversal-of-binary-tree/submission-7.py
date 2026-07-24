# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Store with the levels
        # Check if the root exists first
        if not root:
            return []

        # Array to hold levels
        levels = []

        # Declare stack that stores value with the level
        stack = [(root, 0)]

        # Iterate while the stack exists
        while stack:
            # Pop from the stack
            node, lvl = stack.pop()

            # If the level is greater than the length of the levels, add new list
            if lvl >= len(levels):
                levels.append([])
            
            # Add value to the correct sublist
            levels[lvl].append(node.val)

            # Add values to the stack
            if node.right:
                stack.append((node.right, lvl + 1))
            if node.left:
                stack.append((node.left, lvl + 1))

        return levels
