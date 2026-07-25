# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        DFS Recursive Solution
        Solution Description:
        In this solution, we use the properties of preorder and inorder traversals.
        The first node in the preorder traversal is the root.
        We then find the index where the root is in the inorder array.
            The leftside will be nodes that will be in the left subtree and the rightside will be nodes that will be in the right subtree.
            Also, based on where this index is, we can tell how many nodes will be in each subtree and we use this to partition in the preorder array as it tells us the nodes.
        We then run this recursively for the left and the right subtrees.
            For the left, we pass in the subarray for preorder from 1:mid + 1 and for inorder from 0:mid
            For the right, we pass in the subarray for preorder from mid + 1:end and for inorder from mid + 1:end
        Finally, we return the root
        The only base case is if either array does not exist to return None

        Time: O(n^2)
        Space: O(n)
        """

        # Base Case
        if not preorder or not inorder:
            return None

        # Create the node
        root = TreeNode(preorder[0])
        # Find the index where the root is in inorder
        mid = inorder.index(preorder[0])
        # Call the function on the left and the right
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the root
        return root