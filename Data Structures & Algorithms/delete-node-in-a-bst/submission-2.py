# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Define find_max function within
        # Because within this function, so no need to do self, but still need to pass in positional arguments
        def find_max(root):
            curr = root
            while curr and curr.right:
                curr = curr.right

            # Return the largest node
            return curr
        
        # Base case if the tree is empty to begin with
        if not root:
            return None
        
        # Find the correct value
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Case 1: the value has 0 or 1 child(ren)
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 2: value has 2 children
            else:
                # 2 Ways of doing this: find the MINimum of the right subtree OR the MAXimum of the left subtree
                # Find the maximum value node
                maxVal = find_max(root.left)
                # Reassign root's value to the value of the minVal
                root.val = maxVal.val
                # Rerun the delete on the node you just took to remove the duplicate the inherently exists
                root.left = self.deleteNode(root.left, maxVal.val)

        return root



