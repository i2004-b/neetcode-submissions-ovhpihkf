# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        DFS Recursive Function, optimized.
        Instead of searching the entire array for the index (O(n) for each search), store the indices of each value in a dictionary beforehand
        """
        # Location hashmap to store the indices of the values in the inorder array
        location = {num : index for index, num in enumerate(inorder)}

        # Declare a member value to iterate through preorder
        self.pre_idx = 0

        # Declare helper function
        # The pointers l and r refer to the bounds of inorder
        def dfs(l, r):
            # Base case: if l > r, return None
            if l > r:
                return None

            # Get the root value    
            root_val = preorder[self.pre_idx]
            # Increment self.pre_idx
            self.pre_idx += 1
            # Find where that value is within the inorder array
            mid = location[root_val]

            # Create the root with the value
            root = TreeNode(root_val)
            # Run dfs
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)