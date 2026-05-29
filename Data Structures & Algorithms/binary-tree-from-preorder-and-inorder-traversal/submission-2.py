# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Solution 2:
        Time --> O(n) --> The sequential search through the inorder array is eliminated when using a hashmap and tracking the bounds
        Space --> O(n) --> recursive stack
        """

        # Create hashmap with the inorder items and their indices
        values = {val: ind for ind, val in enumerate(inorder)}

        # Create variable to hold where the root is in the preorder list
        self.pre_ind = 0

        # Create helper function to run the dfs
        def dfs(l, r):
            # If the left pointer exceeds the right, return None
            if l > r:
                return None
            
            # Create the root using the pre_ind
            root = TreeNode(preorder[self.pre_ind])
            # Find where the root is in the inorder array
            mid = values[preorder[self.pre_ind]]
            # Increment pre_ind by 1
            self.pre_ind += 1

            # Recursive call to construct subtrees
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            # Return the constructed tree
            return root
        
        return dfs(0, len(inorder) - 1)

       