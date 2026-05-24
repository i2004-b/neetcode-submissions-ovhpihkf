# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Keep a list outside of the recursive call that can be edited
        levels = []

        # Declare a recursive function that takes in the node and depth
        def dfs(node, depth):
            # Base case: if there is no node, return
            if not node:
                return
            
            # Check the depth; if you are at a new depth, append a list and add the value to that list
            if len(levels) < depth + 1:
                levels.append([])
                
            levels[depth].append(node.val)

            # Call the recursive function on the left and the right, increasing the depth by 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # Run dfs
        dfs(root, 0) # Initial depth is 0

        return levels

