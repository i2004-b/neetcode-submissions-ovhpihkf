# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS Recursive Attempt
        # Define list to store outputs
        right = []

        # Define a helper recursive function
        def dfs(node, depth):
            # Base case: return if the node does not exist
            if not node:
                return
            
            # Add the value to the right list if the depth length == len(right)
            if depth == len(right):
                right.append(node.val)

            # Run the function on the right and left subtrees
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        # Run dfs on the given root node, with depth 0
        dfs(root, 0)

        # Return the list
        return right