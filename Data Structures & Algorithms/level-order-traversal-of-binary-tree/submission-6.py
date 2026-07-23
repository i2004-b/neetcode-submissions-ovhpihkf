# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Hold the result
        res = []

        # Helper function to run dfs
        def dfs(node, lvl):
            # Base Case: if null, return
            if not node:
                return

            # Add the value to the correct sublist by checking length
            if lvl < len(res):
                # Add to appropriate list
                res[lvl].append(node.val)
            else:
                # Add a new list with the value
                res.append([node.val])

            # Call dfs on the left and the right
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        
        dfs(root, 0)
        return res