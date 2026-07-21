# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        stack = [root]
        depths = {None: [True, 0]}

        while stack:
            node = stack[-1]

            if node.left and node.left not in depths:
                stack.append(node.left)
            elif node.right and node.right not in depths:
                stack.append(node.right)
            else:
                # Pop from the stack
                node = stack.pop()

                left_h = depths[node.left][1]
                right_h = depths[node.right][1]
                balance = depths[node.left][0] and depths[node.right][0] and abs(left_h - right_h) <= 1

                depths[node] = [balance, 1 + max(left_h, right_h)]

        return depths[root][0]


