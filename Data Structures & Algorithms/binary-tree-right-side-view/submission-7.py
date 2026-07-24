# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Array to hold solution values
        right = []

        # Helper dfs function to traverse the array
        def dfs(node, lvl):
            # Base case: return if NULL
            if not node:
                return

            # Add the value if the lvl is greater than or equal to the length of right
            if lvl >= len(right):
                right.append(node.val)

            # Go to the right
            dfs(node.right, lvl + 1)
            # Go to the left
            dfs(node.left, lvl + 1)

        # Call function
        dfs(root, 0)
        return right