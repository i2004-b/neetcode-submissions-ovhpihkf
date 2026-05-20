# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive Solution
        # Define array to hold the values of the traversal
        traversal = []

        # Define helper array to go through postorder traversal
        def postorder(root):
            # Base case: if root is NULL, return
            if not root:
                return

            # Postorder Traversal: Left, Right, Root
            postorder(root.left)
            postorder(root.right)
            traversal.append(root.val)

        # Call the postorder function
        postorder(root)

        # Return the traversal array
        return traversal