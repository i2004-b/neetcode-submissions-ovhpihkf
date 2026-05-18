# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create array to hold the values to return 
        visited = []

        # Helper function for traversal
        def preorder(root):
            # Base case: return if the root is NULL
            if not root:
                return

            # Traverse: root, left, right
            visited.append(root.val)
            preorder(root.left)
            preorder(root.right)

        # Call preorder function
        preorder(root)

        # Return visited
        return visited
