"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Postorder simplified is just visit all the children before the parent
        arr = []

        def dfs(root):
            # Base case
            if not root:
                return

            # Go through each child
            for child in root.children:
                # Run dfs for each child
                dfs(child)

            # Add the root value to the array
            arr.append(root.val)

        dfs(root)
        return arr