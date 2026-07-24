# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Hold the rightmost value for each level in a dictionary (map level to value)
        res = {}

        # Create stack initialized with the root and its lvl
        stack = [(root, 0)]

        # Iterate while the stack exists
        while stack:
            # Pop from the stack
            node, lvl = stack.pop()
            
            # Add the node value to the dictionary if node already in it
            if lvl not in res:
                res[lvl] = node.val

            # Add children
            if node.left:
                stack.append((node.left, lvl + 1))
            if node.right:
                stack.append((node.right, lvl + 1))

        # Return the list of results (just the values of dictionary)

        return [val for val in res.values()]