# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            # If the root does not exist, create and return it
        if not root:
            return TreeNode(val)
        
        # Point to the root with curr
        curr = root

        # Iterate while you need to insert into the tree
        while True:
            # If value is greater than the current value, go to the right subtree
            if val > curr.val:
                # If the right pointer is Null, insert the node and return the root
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                # Point to curr.right if it exists
                curr = curr.right
            else:
                # If the value is less than the current value, go to the left subtree
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                # Point to curr.left if it exists
                curr = curr.left