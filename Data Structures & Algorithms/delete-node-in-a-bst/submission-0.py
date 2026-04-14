# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Function to find the minimum of a tree
        def findMin(root):
            curr = root

            while curr and curr.left:
                curr = curr.left
            return curr

        # Return None if there is no root
        if not root:
            return None

        # Find the value
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Case 1: 0 or 1 child(ren)
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 2: 2 children
            else:
                # Find the minimum to change the root with
                minNode = findMin(root.right)
                # Reassign the value of root to the minimum value
                root.val = minNode.val
                # Delete the minimum value that has now become the root value
                root.right = self.deleteNode(root.right, minNode.val)

        return root

        