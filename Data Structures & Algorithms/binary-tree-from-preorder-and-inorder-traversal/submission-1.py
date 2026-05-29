# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Solution 1:
        Time --> O(n^2) --> imerged from the .index() sequentially searching through the array; also complexity arises from recreating arrays
        Space --> O(n) --> recursive stack
        """

        # Base Case: if either list does not exist, return none
        if not preorder or not inorder:
            return None
        
        # Create the root node using preorder[0]
        root = TreeNode(preorder[0])
        # Find the location of the root in the inorder array
        mid = inorder.index(preorder[0])

        # Construct the subtrees recursively
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # Return the root
        return root