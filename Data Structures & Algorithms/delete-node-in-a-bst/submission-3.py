# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Helper function to help find the minimum value
        def minVal(root):
            # Point to the root
            curr = root
            # Loop while curr to ensure that the initial node is Non Null
            # The minimum is the leftmost element
            while curr and curr.left:
                curr = curr.left
            # Return the node itself
            return curr
        
        # Base Case: no root value exists
        if not root:
            return None

        # Search for the value within the tree
        if key > root.val:
            # Search the right side of the tree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # Search the left side of the tree
            root.left = self.deleteNode(root.left, key)
        # What to do once you find the value
        else:
            # Case 1: 0 or 1 child(ren)
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 2:
            else:
                # Find the minimum in the right subtree using the helper function
                minValNode = minVal(root.right)
                # Replace the root value with the minimum value
                root.val = minValNode.val
                # Delete the duplicate of the minValNode
                root.right = self.deleteNode(root.right, minValNode.val)

        return root