# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Create and return node if root is empty
        if not root:
            return TreeNode(val)

        # Assign curr to point to root
        curr = root

        # Keep looping until you insert the node
        while True:
            # Check if the val to insert is greater than the curr
            if val > curr.val:
                # If it points to Null, create the node
                if not curr.right:
                    curr.right = TreeNode(val)
                    # Break the loop
                    break
                # If right pointer does exist, reassign curr
                curr = curr.right
            # Otherwise val is less than curr
            elif val < curr.val:
                # If it points to Null create the node
                if not curr.left:
                    curr.left = TreeNode(val)
                    # Break the loop
                    break
                # Reassign curr if the node exists
                curr = curr.left
        
        # Return root of tree
        return root
