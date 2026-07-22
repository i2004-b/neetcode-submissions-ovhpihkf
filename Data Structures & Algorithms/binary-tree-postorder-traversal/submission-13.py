# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visited = [False]
        arr = []

        while stack:
            # Pop
            node, visit = stack.pop(), visited.pop()

            if node:
                if visit:
                    arr.append(node.val)
                else: # Add back and add the children
                    stack.append(node)
                    visited.append(True)
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)

        return arr
