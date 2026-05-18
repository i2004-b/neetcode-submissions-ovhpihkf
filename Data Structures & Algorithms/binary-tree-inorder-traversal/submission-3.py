# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Declare array to store the values to return
        visited = []

        # Declare helper function for recursive inorder traversal
        def inorder(root):
            # Base case: if the root is NULL
            if not root:
                return

            # Inorder traversal is Left --> Root --> Right
            inorder(root.left)
            visited.append(root.val)
            inorder(root.right)

        # Call the inorder function
        inorder(root)

        # Return the list
        return visited