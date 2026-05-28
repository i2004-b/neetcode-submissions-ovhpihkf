# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base Case: if the lists do not exist, return None
        if not preorder or not inorder:
            return None

        # Create the root --> index 1 of preorder
        root = TreeNode(preorder[0])

        # Find the root's index in the inorder list
        # The numbers before it will be in L subtree and the numbers after will be in the R subtree
        # For example, if mid is index 3
        # The left subtree will have 3 items (length of 3)
        # The right subtree will have the remaining elements
        mid = inorder.index(preorder[0])

        # Recursively call the function on the left and the right subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return root
        return root
