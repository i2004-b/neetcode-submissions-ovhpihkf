"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # Iterative
        # Have a stack and track if the children have been visited
        stack = [(root, False)]

        arr = []

        # Iterate while the stack exists
        while stack:
            node, visit = stack.pop()

            if node:
                if visit:
                    arr.append(node.val)
                else:
                    # Add value back to stack
                    stack.append((node, True))
                    # Add children
                    for child in node.children[::-1]:
                        stack.append((child, False))

        return arr