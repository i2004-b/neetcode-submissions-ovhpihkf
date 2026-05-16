# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS implementation attempt --> Done after looking at Neetcode nodes
        # Create empty array to hold sub-arrays for each level
        res = []

        # Declare helper function for DFS
        def dfs(node, depth):
            # Base case: the node is NULL
            if not node:
                return

            # Check if the subarray for the given depth exists:
            if len(res) < depth + 1:
                res.append([])

            # Add the current value to the appropriate subarray
            res[depth].append(node.val)

            # Run the recursive algorithm on the children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # Run dfs on the tree
        dfs(root, 0)
        # Return the whole list of all levels
        return res