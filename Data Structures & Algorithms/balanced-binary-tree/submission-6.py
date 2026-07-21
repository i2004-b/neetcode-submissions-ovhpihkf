# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS Recursive Solution
        # Complexity:
        # Time: O(n)
        # Space: O(n)

        def dfs(root):
            # Base Case
            if not root:
                # Return that it is balanced with a height of 0
                return [True, 0]

            # Check the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Check balance of the current node using the heights
            if abs(left[1] - right[1]) <= 1:
                balance = True
            else:
                balance = False

            # Return the list with balance (needs to be anded with the booleans of the left and right) and the height
            return [balance and left[0] and right[0], 1 + max(left[1], right[1])]

        return dfs(root)[0]


